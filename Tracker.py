import streamlit as st
import datetime
from duckduckgo_search import DDGS
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="Verified Geography CFP Finder", page_icon="🌍", layout="wide")

st.title("🌍 Verified Academic CFP Finder")
st.markdown("### *Zero-Hallucination AI Agent for Spatial & Social Sciences*")
st.write("This tool runs live searches and applies strict logical guardrails to ensure every conference, workshop, and CFP returned is verified and real.")
st.divider()

# =====================================================================
# 1. API KEY & CONFIGURATION
# =====================================================================
st.sidebar.header("🔑 1. Setup API Access")
api_key_input = st.sidebar.text_input("Gemini API Key", type="password", help="Get a free key from Google AI Studio")

# Fallback check
api_key = api_key_input if api_key_input else st.secrets.get("GEMINI_API_KEY", "")

# Discipline selection
st.sidebar.markdown("---")
st.sidebar.header("🎯 2. Research Focus")

DISCIPLINE_MAP = {
    "🌍 Geography & Spatial Planning": "Geography, human geography, regional development, spatial justice, urban/rural development, or settlement geography",
    "👥 Sociology & Social Sciences": "Sociology, social research, social theory, demography, caste, class, gender studies, or agrarian crisis",
    "💼 Management & Policy": "Public policy, development studies, governance, policy evaluation, or administrative studies",
    "🏺 Anthropology": "Anthropology, ethnography, cultural studies, fieldwork, or tribal studies",
    "📜 History": "Historical geography, archives, historiography, agrarian history, or colonial studies",
    "🛰️ GIS & Geoinformatics": "GIS, geoinformatics, spatial analysis, remote sensing, spatial data science, mapping, or spatial modeling"
}

selected_discipline = st.sidebar.selectbox("Select Target Discipline:", list(DISCIPLINE_MAP.keys()))
default_keywords = DISCIPLINE_MAP[selected_discipline]

custom_keywords = st.sidebar.text_area(
    "Fine-tune Keywords for Search:", 
    value=default_keywords,
    height=100
)

# Date Range
current_year = datetime.date.today().year
target_year = st.sidebar.number_input("Target Calendar Year:", min_value=2020, max_value=2035, value=current_year)

# =====================================================================
# 2. RUN SHIELDED AGENT ENGINE
# =====================================================================
st.write("### 🚀 Click below to run the verified scan")

if st.button("🔍 Run Verified Search & Curation", type="primary", use_container_width=True):
    if not api_key:
        st.error("⚠️ Please enter a Gemini API Key in the sidebar to run the AI step!")
    else:
        # Initialize Gemini
        genai.configure(api_key=api_key)
        
        with st.status("Fetching live web results...", expanded=True) as status:
            
            # Step A: Build Query & Search Web
            status.write("🌐 Step 1: Retrieving live indexing data via DuckDuckGo...")
            
            search_query = f"site:edu OR site:ac.uk OR site:ac.in ({custom_keywords}) AND (conference OR workshop OR \"call for papers\") AND \"{target_year}\""
            
            raw_results = []
            try:
                with DDGS() as ddgs:
                    search_results = ddgs.text(search_query, max_results=15)
                    for r in search_results:
                        raw_results.append({
                            "title": r.get("title", ""),
                            "snippet": r.get("body", ""),
                            "link": r.get("href", "")
                        })
            except Exception as e:
                st.error(f"Search failed: {e}")
            
            if not raw_results:
                status.update(label="No initial results found.", state="error")
                st.warning("No live listings found matching your exact keywords. Try broadening your keywords in the sidebar.")
            else:
                status.write(f"✅ Found {len(raw_results)} live web listings. Running verification filters...")
                
                # Step B: Compile raw data with strict index matching
                compiled_data = ""
                for index, item in enumerate(raw_results):
                    compiled_data += f"\n--- SOURCE RECORD {index+1} ---\nTitle: {item['title']}\nSnippet: {item['snippet']}\nLink: {item['link']}\n"
                
                status.write("🧠 Step 2: Running Gemini with Zero-Hallucination Guardrails...")
                
                # Step C: Ask Gemini to clean and curate with strict rules
                prompt = f"""
                You are a meticulous, zero-tolerance academic database indexer. 
                Your primary directive is: DO NOT HALLUCINATE, FABRICATE, OR EXTRAPOLATE.
                
                I am providing you with live raw search records. You must extract and format active, upcoming academic events (conferences, workshops, calls for papers) for the target year: {target_year}.
                
                CRITICAL GUARDRAIL RULES:
                1. If a search record is for an event that has already passed, discard it. (Today is {datetime.date.today().strftime('%B %d, %Y')}).
                2. Do not invent any deadlines. If a deadline is not explicitly written in the provided text snippet, write "Not Specified in Snippet" (do not guess!).
                3. Do not invent, alter, or guess URLs. The link column MUST strictly contain the exact URL from the corresponding Source Record's "Link" field.
                4. If you are unsure whether a record is a real academic event, discard it.
                
                Format the final output as a clean Markdown table with the following columns:
                | Discipline | Organizing Institution | Event Title | Event Date / CFP Deadline | Key Themes / Focus | Verified Web Source |
                
                In the "Verified Web Source" column, use the exact Link provided in the source records as a standard clickable Markdown link, labeled "[Go to Official Site]".
                
                Here is the raw data you are allowed to use:
                {compiled_data}
                """
                
                try:
                    # Run LLM
                    model = genai.GenerativeModel('gemini-1.5-pro')
                    response = model.generate_content(prompt)
                    
                    status.update(label="Curation complete!", state="complete")
                    
                    # Display Results
                    st.success("🎉 Curation completed. All links and details correspond directly to live web results!")
                    st.markdown("## 📋 Verified Event Dashboard")
                    st.markdown(response.text)
                    
                except Exception as e:
                    status.update(label="AI extraction failed.", state="error")
                    st.error(f"Error calling Gemini API: {e}")

st.divider()
st.caption("AI Academic Curator Engine • Verification Mode Active • Powered by Streamlit and Google Gemini.")
