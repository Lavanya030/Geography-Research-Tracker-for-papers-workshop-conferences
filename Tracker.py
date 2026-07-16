import datetime
import streamlit as st
from duckduckgo_search import DDGS

# Set up page configurations at the absolute top
st.set_page_config(page_title="Global Geography Discovery Engine", page_icon="🌍", layout="wide")

# =====================================================================
# 1. THE GEOGRAPHY DISCIPLINARY SEED DICTIONARY
# =====================================================================
SEEDS = {
    "1. GIS, Tech, Data Science & GeoAI": [
        "GeoAI", "Spatial Informatics", "Digital Twin", "Geodesy", 
        "GIScience", "Remote Sensing", "Geoinformatics", "Spatial AI"
    ],
    "2. Human, Social, Class & Labor": [
        "Socio-Physical Geography", "Regional Development", "Spatial Justice", 
        "Abolition Geographies", "Black Urbanism", "Geographies of Memory"
    ],
    "3. Urban, Megacities & Logistics": [
        "Smart Mobility", "Logistics & Supply Chain", "Peri-Urban Informatics", 
        "Megacities", "Planetary Urbanisation", "Urban Informatics"
    ],
    "4. Physical Landscapes & Earth Surface Dynamics": [
        "Climate Change and Extreme Events", "Hydro-Social Dimensions", "Eco-Acoustics", 
        "Tephrochronology", "Alpine Ecology", "Karst Geomorphology"
    ],
    "5. Resource, Food & Environmental Governance": [
        "Food Security", "Food Systems", "Food Sovereignty", "Agroecology", "Political Ecology"
    ],
    "11. Marginal, Smart & Health Geographies": [
        "Smart Geographies", "Smart Governance", "Marginalized Spaces", 
        "Health Geographies", "Spatial Epidemiology", "Therapeutic Landscapes"
    ]
}

INDIAN_ACADEMIC_PROTOCOLS = {
    "honorifics": ["Chief Patron", "Hon'ble Vice-Chancellor", "Organizing Secretary", "Convenor"],
    "grants": ["ICSSR Sponsored", "DST-SERB", "UGC-SAP", "Indian Knowledge System (IKS)", "Viksit Bharat"]
}

# =====================================================================
# 2. INTERFACE BUILDER
# =====================================================================
st.title("🌍 Global Academic Geography Discovery Engine")
st.markdown("### *Live Real-Time Academic Event & CFP Web Searcher*")
st.divider()

# Sidebar Setup
st.sidebar.header("🔍 Search Parameters")
target_region = st.sidebar.selectbox("1. Target Institutional Tier", [
    "India Tier (IITs/Central Universities)", 
    "United States Tier (.edu)", 
    "United Kingdom Tier (.ac.uk)"
])
selected_category = st.sidebar.selectbox("2. Select Core Discipline", list(SEEDS.keys()))
selected_keyword = st.sidebar.selectbox("3. Select Refined Semantic Keyword", SEEDS[selected_category])

# Set live timing metrics
current_date = datetime.date.today()
st.sidebar.info(f"📅 Today's Date: {current_date.strftime('%B %d, %Y')}")

# =====================================================================
# 3. LIVE WEB SCRAPER LOGIC (DUCKDUCKGO INTERACTIVE AGENT)
# =====================================================================
# Build targeted academic syntax hooks to filter out spam
site_hook = "site:.ac.in" if "India" in target_region else ("site:.edu" if "United States" in target_region else "site:.ac.uk")

# Indian universities usually publish "brochures" or "circulars"
if "India" in target_region:
    intent_hook = '("conference" OR "workshop" OR "call for papers" OR "brochure" OR "circular")'
    # Force search to check for ICSSR, DST or typical administrative headers to ensure institutional legitimacy
    query = f'{site_hook} "{selected_keyword}" AND {intent_hook} AND ("ICSSR" OR "sponsored" OR "university" OR "seminar")'
else:
    intent_hook = '("conference" OR "symposium" OR "workshop" OR "call for papers")'
    query = f'{site_hook} "{selected_keyword}" AND {intent_hook}'

st.subheader(f"📊 Live Search: '{selected_keyword}' events in {target_region}")
st.markdown("This section bypasses third-party aggregator sites and pulls live event pages directly from real university subdomains.")

# Execute live scrape when requested
if st.button("🚀 Fetch Live Web Results", use_container_width=True):
    with st.spinner(f"Querying public university servers for '{selected_keyword}'..."):
        try:
            # Initialize DuckDuckGo live API search client
            with DDGS() as ddgs:
                # Restrict search results to return fresh, relevant matches
                search_results = list(ddgs.text(query, max_results=10))
                
            if search_results:
                st.success(f"Found {len(search_results)} live entries on official university websites!")
                
                for idx, result in enumerate(search_results):
                    # Clean up the output cards
                    with st.container():
                        st.markdown(f"#### {idx+1}. {result['title']}")
                        st.write(result.get('body', 'No description preview available.'))
                        st.markdown(f"🔗 [Visit Official Institutional Page]({result['href']})")
                        st.divider()
            else:
                st.warning("⚠️ No active notices found matching this specific keyword combination on the servers today.")
                st.info("Try switching the **Target Institutional Tier** or selecting a broader semantic keyword in the sidebar.")
                
        except Exception as e:
            st.error("Error executing live connection.")
            st.write(f"Details: {str(e)}")
            st.info("If you just added `duckduckgo-search` to requirements.txt, ensure Streamlit Cloud has finished rebuilding the app environment.")
else:
    st.info("💡 Click the button above to execute a real-time crawl of university directories.")

st.sidebar.markdown("---")
st.sidebar.markdown("**Engine Search String:**")
st.sidebar.code(query, language="sql")
