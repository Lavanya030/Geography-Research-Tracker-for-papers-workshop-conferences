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
# 3. DYNAMIC QUERY CONSTRUCTOR (FALLBACK LOGIC)
# =====================================================================
site_hook = "site:.ac.in" if "India" in target_region else ("site:.edu" if "United States" in target_region else "site:.ac.uk")

# Strict, highly targeted query (Primary Attempt)
if "India" in target_region:
    strict_query = f'{site_hook} "{selected_keyword}" (conference OR workshop OR seminar) (ICSSR OR UGC OR DST)'
else:
    strict_query = f'{site_hook} "{selected_keyword}" (conference OR symposium OR workshop OR "call for papers")'

# Broad query (Secondary Fallback Attempt if strict returns 0 results)
broad_query = f'{site_hook} "{selected_keyword}" (conference OR workshop OR CFP OR seminar)'

st.subheader(f"📊 Live Search: '{selected_keyword}' events in {target_region}")
st.markdown("This search queries official university servers directly to find conferences, workshops, and calls for papers.")

# =====================================================================
# 4. EXECUTION
# =====================================================================
if st.button("🚀 Fetch Live Web Results", use_container_width=True):
    with st.spinner(f"Querying university servers for '{selected_keyword}'..."):
        results = []
        try:
            # 1. Attempt strict targeted academic search
            with DDGS() as ddgs:
                results = list(ddgs.text(strict_query, max_results=8))
            
            # 2. If nothing is found, auto-fallback to the relaxed/broader query
            if not results:
                st.info("🔄 Optimizing query filters to surface broader results...")
                with DDGS() as ddgs:
                    results = list(ddgs.text(broad_query, max_results=8))
                    
            if results:
                st.success(f"Found {len(results)} live listings!")
                for idx, result in enumerate(results):
                    with st.container():
                        st.markdown(f"#### {idx+1}. {result['title']}")
                        st.write(result.get('body', 'No description preview available.'))
                        st.markdown(f"🔗 [Visit Official Institutional Page]({result['href']})")
                        st.divider()
            else:
                st.warning("⚠️ No active notices found matching this specific keyword combination.")
                st.info("Tip: Try searching a related sister keyword in the sidebar or check another Tier region.")
                
        except Exception as e:
            st.error("Connection failed. The search API rate-limit might have triggered.")
            st.write(f"Technical Log: {str(e)}")
else:
    st.info("💡 Click the button above to execute a real-time crawl of university directories.")

st.sidebar.markdown("---")
st.sidebar.markdown("**Active Query:**")
st.sidebar.code(strict_query, language="sql")
st.sidebar.markdown("**Fallback Query:**")
st.sidebar.code(broad_query, language="sql")
