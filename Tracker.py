import streamlit as st
import requests
import urllib.parse

# Set up page configurations at the absolute top
st.set_page_config(page_title="Global University Geography Tracer", page_icon="🌍", layout="wide")

st.title("🌍 Global University Geography Tracer")
st.markdown("### *Dynamic Notice-Board & Research Group Discovery Engine*")
st.write("Using a live international directory, pick any nation and university to instantly trace their official geography departments, calendars, and active workshops.")
st.divider()

# =====================================================================
# 1. LIVE COUNTRY & UNIVERSITY API CONNECTION
# =====================================================================
# Popular nations to list in the sidebar (User can select any)
POPULAR_COUNTRIES = [
    "India", "United Kingdom", "United States", "Canada", "Australia", 
    "Germany", "France", "Netherlands", "Singapore", "South Africa", 
    "Japan", "Sweden", "Switzerland", "Brazil"
]

st.sidebar.header("🗺️ Select Target Territory")
selected_country = st.sidebar.selectbox("1. Choose a Country", POPULAR_COUNTRIES)

# Helper function to fetch real-time university database records
@st.cache_data(show_spinner="Connecting to global university registries...")
def fetch_universities_by_country(country_name):
    try:
        # Querying the Hipolabs open directory database
        api_url = f"http://universities.hipolabs.com/search?country={urllib.parse.quote_plus(country_name)}"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Sort alphabetically by name
            return sorted(data, key=lambda x: x["name"])
    except Exception as e:
        st.sidebar.error(f"Failed to fetch directory: {e}")
    return []

# Fetch live list
uni_list = fetch_universities_by_country(selected_country)

if uni_list:
    uni_names = [uni["name"] for uni in uni_list]
    selected_uni_name = st.sidebar.selectbox("2. Select an Institution", uni_names)
    
    # Retrieve details of selected university
    selected_uni_data = next(item for item in uni_list if item["name"] == selected_uni_name)
    # Extract domain (e.g., "jnu.ac.in" or "ox.ac.uk")
    uni_domain = selected_uni_data["domains"][0] if selected_uni_data.get("domains") else ""
    uni_website = selected_uni_data["web_pages"][0] if selected_uni_data.get("web_pages") else ""
else:
    st.sidebar.warning("No universities found or registry is currently offline.")
    selected_uni_name = None
    uni_domain = ""
    uni_website = ""

# =====================================================================
# 2. DISCOVERY & SEARCH FORMULATION PANELS
# =====================================================================
if selected_uni_name and uni_domain:
    col_info, col_search = st.columns([1, 1], gap="large")
    
    with col_info:
        st.subheader("🏫 Selected Institutional Node")
        st.markdown(f"### {selected_uni_name}")
        st.markdown(f"**Country Registry:** `{selected_country}`")
        st.markdown(f"**Primary Web Domain:** `{uni_domain}`")
        
        if uni_website:
            st.link_button("🌐 Open Main University Portal", uni_website, use_container_width=True)
        
        st.divider()
        st.markdown(
            """
            #### How to use this:
            Since universities house their notice boards differently (some call them 'Seminars', others 'CFPs', 'Workshops', or 'Circulars'), we have built search query formulas that target the selected university's subdomains. 
            
            Clicking a search button will open a new browser tab with your custom search query already prepared.
            """
        )

    with col_search:
        st.subheader("🔍 Automated Discovery Filters")
        st.write("Select a targeted academic path to generate custom direct links:")
        
        # Select what kind of workspace to search for
        academic_path = st.radio(
            "What geography space are you looking for?",
            options=[
                "Department & Faculty (Socio-Spatial/GIS/Human Geography)",
                "Workshops, Seminars & Active Notice Boards",
                "Research Labs & Working Groups",
                "Calls for Papers (CFP) & Regional Symposia"
            ],
            index=1
        )
        
        # Build precise search logic based on selection
        if "Department" in academic_path:
            raw_query = f'site:{uni_domain} ("geography department" OR "geography faculty" OR "spatial sciences")'
        elif "Workshops" in academic_path:
            raw_query = f'site:{uni_domain} "geography" AND ("workshop" OR "seminar series" OR "event schedule" OR "notice board" OR "events calendar")'
        elif "Labs" in academic_path:
            raw_query = f'site:{uni_domain} "geography" AND ("research lab" OR "working group" OR "centre for" OR "consortium")'
        else:
            raw_query = f'site:{uni_domain} "geography" AND ("call for papers" OR "CFP" OR "abstract submission" OR "symposium")'
            
        # Encode URL for safe redirection
        encoded_query = urllib.parse.quote_plus(raw_query)
        google_search_url = f"https://www.google.com/search?q={encoded_query}"
        bing_search_url = f"https://www.bing.com/search?q={encoded_query}"
        
        st.markdown("#### 🚀 Trace Direct Channels")
        st.link_button("🌐 Search Google for this University's Geography Space", google_search_url, use_container_width=True, type="primary")
        st.link_button("🔍 Search Bing for this University's Geography Space", bing_search_url, use_container_width=True)
        
        st.markdown("---")
        st.write("**Target Domain Search Formula:**")
        st.code(raw_query, language="sql")
        st.caption("💡 *This custom formula forces search engines to show only relevant results from within this specific university's servers, bypassing generic advertisement sites.*")

else:
    st.info("👈 Use the controls on the left to select a country and university to begin!")

st.divider()
st.caption("🛡️ Global Geography Discovery Hub © 2026. Self-healing country registry bypass active.")
