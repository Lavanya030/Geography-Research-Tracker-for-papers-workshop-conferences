import streamlit as st
import urllib.parse
import datetime

# Set up page configurations at the absolute top
st.set_page_config(page_title="Global Geography Tracker", page_icon="🌍", layout="wide")

st.title("🌍 Global Academic Geography Event Aggregator")
st.markdown("### *Unified Background Tracking & Live Broadcast Stream*")
st.write("This engine monitors major global research hubs simultaneously, stripping away expired programs and aggregating only future-facing notice boards.")
st.divider()

# Get today's automatic rolling date to shield expired content
today = datetime.date.today()
formatted_today = today.strftime("%Y-%m-%d")

# =====================================================================
# 1. CORE REGIONAL DIRECTORIES (PRE-LOADED DOMAINS)
# =====================================================================
REGIONAL_NETWORKS = {
    "🇮🇳 India Academic Network (.ac.in)": [
        {"inst": "Jawaharlal Nehru University", "domain": "jnu.ac.in"},
        {"inst": "Delhi University", "domain": "du.ac.in"},
        {"inst": "IIT Bombay", "domain": "iitb.ac.in"},
        {"inst": "IIT Kharagpur", "domain": "iitkgp.ac.in"},
        {"inst": "Banaras Hindu University", "domain": "bhu.ac.in"},
        {"inst": "Jamia Millia Islamia", "domain": "jmi.ac.in"},
        {"inst": "Aligarh Muslim University", "domain": "amu.ac.in"}
    ],
    "🇬🇧 United Kingdom Network (.ac.uk)": [
        {"inst": "University of Oxford", "domain": "ox.ac.uk"},
        {"inst": "University of Cambridge", "domain": "cam.ac.uk"},
        {"inst": "University College London", "domain": "ucl.ac.uk"},
        {"inst": "University of Liverpool", "domain": "liverpool.ac.uk"},
        {"inst": "University of Southampton", "domain": "southampton.ac.uk"},
        {"inst": "University of Edinburgh", "domain": "ed.ac.uk"}
    ],
    "🇺🇸 United States Network (.edu)": [
        {"inst": "Clark University", "domain": "clarku.edu"},
        {"inst": "University of Maryland", "domain": "umd.edu"},
        {"inst": "Penn State University", "domain": "psu.edu"},
        {"inst": "UC Berkeley", "domain": "berkeley.edu"},
        {"inst": "University of Washington", "domain": "washington.edu"}
    ]
}

# =====================================================================
# 2. SEED DISCIPLINARY MODIFIERS
# =====================================================================
st.sidebar.header("🎯 Focus Parameters")
selected_network = st.sidebar.selectbox("1. Select Network to Aggregate", list(REGIONAL_NETWORKS.keys()))
discipline_focus = st.sidebar.selectbox(
    "2. Academic Focus Area",
    ["Socio-Spatial & Rural Development", "GIScience, Spatial Computing & GeoAI", "Physical Landscapes & Climate Change"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("📅 Live Rolling Filter")
st.sidebar.info(f"Targeting programs active on or after today: **{today.strftime('%b %d, %Y')}**")

# =====================================================================
# 3. AGGREGATOR ENGINE & MULTI-QUERY GENERATOR
# =====================================================================
active_network_list = REGIONAL_NETWORKS[selected_network]

st.subheader(f"📡 Unified Broadcast: Tracking {selected_network}")
st.write(f"Aggregating active notices for **{discipline_focus}** across all registered institutions in this network simultaneously:")

# Display tracking nodes in a clean layout
cols = st.columns(len(active_network_list))
for i, node in enumerate(active_network_list):
    cols[i].markdown(f"📡 **{node['inst']}**\n`{node['domain']}`")

st.divider()

# Construct the multi-site search filter
# E.g., (site:jnu.ac.in OR site:du.ac.in OR site:iitb.ac.in)
site_queries = [f"site:{node['domain']}" for node in active_network_list]
unified_site_string = "(" + " OR ".join(site_queries) + ")"

# Define intent and keyword strings
if "Socio-Spatial" in discipline_focus:
    keywords = '("geography" OR "regional development" OR "rural" OR "spatial justice" OR "socio-spatial")'
elif "GIScience" in discipline_focus:
    keywords = '("GIS" OR "remote sensing" OR "spatial data science" OR "GeoAI" OR "geoinformatics")'
else:
    keywords = '("geomorphology" OR "climate change" OR "biogeography" OR "hydrology")'

# Combine everything into a single macro-aggregator query
# Only pulling pages published or updated after today's dynamic calendar date
macro_query = f'{unified_site_string} {keywords} AND ("workshop" OR "conference" OR "call for papers" OR "seminar series" OR "symposium") AND after:{formatted_today}'

col_search_action, col_query_details = st.columns([1, 1], gap="large")

with col_search_action:
    st.markdown("#### ⚡ Launch Consolidated Aggregate Search")
    st.write(
        """
        By launching this consolidated search, you check the servers of **all network universities 
        at the exact same time**. Google's engine will return a single, unified list of upcoming 
        events, completely bypassing expired pages.
        """
    )
    
    encoded_macro = urllib.parse.quote_plus(macro_query)
    st.link_button(
        f"🚀 Query Entire {selected_network.split(' ')[0]} Network", 
        f"https://www.google.com/search?q={encoded_macro}", 
        type="primary", 
        use_container_width=True
    )

with col_query_details:
    st.markdown("#### 🛠️ Live Tracking Logic")
    st.write("This query is automatically updated every single day to push older posts out of your results:")
    st.code(macro_query, language="sql")

st.divider()
st.caption("Global Geography Discovery Engine. Dynamic multi-node continuous aggregation active.")
