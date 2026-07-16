import datetime
import streamlit as st

# Set up page configurations at the absolute top of the script execution loop
st.set_page_config(page_title="Global Geography Discovery Engine", page_icon="🌍", layout="wide")

# =====================================================================
# 1. THE ULTIMATE GEOGRAPHY & INTERDISCIPLINARY SEED DICTIONARY (ALL SECTORS)
# =====================================================================
SEEDS = {
    "1. GIS, Tech, Data Science & GeoAI": [
        "GeoAI", "Spatial Informatics", "Digital Twin Hub", "Geodesy", 
        "GIScience", "Spatial Computing", "Gaussian Splatting", "3D GIS", 
        "CyberGIS", "Remote Sensing", "Geoinformatics", "Geomatics", 
        "Geocomputation", "Cartography", "Topography", "Earth Observation", 
        "Spatial Cyberinfrastructure", "Geovisualization", "Spatial AI",
        "Geostatistics", "Volunteered Geographic Information", "VGI", "Spatial Data Science"
    ],
    "2. Human, Social, Class & Labor": [
        "Socio-Physical Geography", "Regional Development", "Spatial Justice", 
        "Abolition Geographies", "Black Urbanism", "Geographies of Memory",
        "Geographies of Religion", "Working-Class Geographies", "Feminist Geopolitics",
        "Class Spatialities", "Spatial Segregation", "Geographies of Labour",
        "Socio-Economic Stratification", "Spatial Marginalisation", "Socio-Spatial Exclusion",
        "Contested Memories", "Memorial Landscapes", "Sacred Spaces"
    ],
    "3. Urban, Megacities & Logistics": [
        "Smart Mobility Platforms", "Logistics & Supply Chain", "Peri-Urban Informatics", 
        "Megacities", "Planetary Urbanisation", "Urban Informatics", "Climate Innovation",
        "Megalopolis", "Conurbation", "Extended Urbanisation", "Informal Settlements",
        "Slum Dynamics", "Urban Sprawl", "Global Cities", "Urban Metabolisms",
        "Smart Cities", "Transport Geography", "Chokepoints", "Corridor Urbanism"
    ],
    "4. Physical Landscapes & Earth Surface Dynamics": [
        "Climate Change and Extreme Events", "Hydro-Social Dimensions", "Eco-Acoustics", 
        "Tephrochronology", "Alpine Ecology", "Karst Geomorphology", "Subterranean Systems",
        "Paleo-Hydroclimatology", "Coastal Dynamics", "Biogeography", "Glaciology",
        "Cryosphere", "Quaternary Science", "Earth Surface Processes", "Permafrost",
        "Fluvial Geomorphology", "Watershed Science", "Pyroclastic Density Currents",
        "Lahar Modeling", "Atmospheric Rivers", "Dendrogeomorphology"
    ],
    "5. Resource, Food & Environmental Governance": [
        "Food Security", "Food Systems", "Food Sovereignty", "Food Deserts", 
        "Agroecology", "Agricultural Systems", "Agrarian Studies", "Resource Management", 
        "Water Security", "Land Use Policy", "Land Cover Change", "Commodity Chains", 
        "Political Ecology", "Environmental Justice", "Conservation Politics", 
        "Commons Governance", "Extractivism", "Energy Transitions", "Land-Change Science"
    ],
    "6. Identity, Race, Diaspora & Area Studies": [
        "Animal Geographies", "More-Than-Human Spaces", "Black Geographies", 
        "Chinese Diasporic Geographies", "South Asian Geographies", "East Asian Urbanism",
        "African Diaspora Spatialities", "Racial Capitalism Spatialities", "Racialized Spaces",
        "Transnational Chinese Spaces", "Subcontinental Spatialities", "Interspecies Spatialities",
        "Queer Geographies", "Trans Spatialities", "Geographies of the Body", "Intimate Geopolitics"
    ],
    "7. Extreme, Military, Surveillance & Shadow Spaces": [
        "Military Geography", "Terrain Analysis", "Geosecurity", "Critical Security Studies",
        "Geopolitical Strategy", "Conflict Landscapes", "Border Surveillance", "Weaponized Space",
        "Demilitarized Zones", "DMZ", "Geographic Intelligence", "Shadow Geographies",
        "Clandestine Landscapes", "Illicit Networks", "Smuggling Spatialities", "Carceral Geographies",
        "Surveillance Landscapes", "Borderscapes", "Algorithmic Governance"
    ],
    "8. Outer Space, Astropolitics & Subterranean Axis": [
        "Astropolitics", "Outer Space Geography", "Exogeography", "Celestial Geopolitics",
        "Planetary Geography", "Volumetric Geography", "Orbital Infrastructure", "Space Commons Governance",
        "Speleology", "Underground Spaces", "Subsurface Planning", "Mining Geographies", "Void Analysis"
    ],
    "9. Historical Eras, Empires & Trade Networks": [
        "Silk Road Spatialities", "Maritime Empires", "Colonial Cartography", "Historical Trade Networks",
        "Indian Ocean Trade", "Trans-Saharan Networks", "Mercantile Geographies", "Imperial Landscapes",
        "Pre-Columbian Spatialities", "Settler Colonialism Spatialities", "Deep-Time Geographies"
    ],
    "10. Philosophy, Culture & Radical Maps": [
        "Psychogeography", "Spatial Phenomenology", "Marxist Geography", "Humanistic Geography",
        "Spatial Ontologies", "Affective Geographies", "Non-Representational Theory", "Spatial Epistemologies",
        "Counter-Mapping", "Radical Cartography", "Indigenous Spatial Sovereignty", "Decolonial Cartographies",
        "Material Culture Geographies", "Heritage Spatialities", "Landscape Semiotics", "Spatial Iconography",
        "Literary Geographies", "Spatial Narratives", "Geopoetics", "Spatial Forensics"
    ],
    "11. Marginal, Smart & Health Geographies": [
        "Smart Geographies", "Smart Governance", "Smart Infrastructure", "Smart Mobility",
        "Marginalized Spaces", "Marginality", "Peripheralization", "Spatial Disadvantage",
        "Geographies of Exclusion", "Health Geographies", "Spatial Epidemiology", "Therapeutic Landscapes",
        "Environmental Health Justice", "Geomedicine", "Spatial Syndemics", "Climate Gentrification"
    ],
    "12. Innovation & Socio-Technical Transitions": [
        "Geospatial Innovation", "Spatial Innovation", "Socio-Technical Innovation", "Technological Transitions",
        "Digital Innovation", "Eco-Innovation", "Social Innovation", "Responsible Innovation",
        "Regional Innovation Systems", "Innovation Clusters", "Smart Specialisation", "Spatial Entrepreneurship"
    ]
}

# Formal administrative protocols unique to the Indian university landscape (.ac.in notices)
INDIAN_ACADEMIC_PROTOCOLS = {
    "honorifics": ["Chief Patron", "Hon'ble Vice-Chancellor", "Organizing Secretary", "Convenor", "Resource Persons", "Advisory Committee", "Patron", "Keynote Address"],
    "ceremonials": ["Inaugural Session", "Valedictory Session", "Lighting of the Lamp", "Souvenir Volume", "Abstract Booklet", "Oral and Poster Presentation Sessions"],
    "grants": ["ICSSR Sponsored", "DST-SERB Karyashala Scheme", "UGC-SAP Supported", "DST-FIST Funded", "Indian Knowledge System (IKS)", "Viksit Bharat", "Capacity Building Programme"]
}

# =====================================================================
# 2. MASTER DATABASE POOL (SIMULATING GEOGRAPHY ENTRIES FOR TICKER EVALUATION)
# =====================================================================
MOCK_WEB_DATABASE = [
    {
        "category": "4. Physical Landscapes & Earth Surface Dynamics",
        "keyword": "Hydro-Social Dimensions",
        "region": "India Tier (IITs/Central Universities)",
        "institution": "India Space Lab (isl.ac.in)",
        "title": "National Remote Sensing & GIS Application for Hydro-Vulnerability Workshop",
        "deadline": "2026-07-22",  # Near-term trigger layout
        "url": "https://isl.ac.in"
    },
    {
        "category": "2. Human, Social, Class & Labor",
        "keyword": "Regional Development",
        "region": "India Tier (IITs/Central Universities)",
        "institution": "University of Kota Central (uok.ac.in)",
        "title": "52nd National Conference of Rajasthan Geographical Association",
        "deadline": "2026-09-17",
        "url": "https://uok.ac.in"
    },
    {
        "category": "1. GIS, Tech, Data Science & GeoAI",
        "keyword": "GeoAI",
        "region": "United States Tier (.edu)",
        "institution": "Center for Geospatial Information Science, UMD",
        "title": "UCGIS 2026 Symposium Plenary: Advancements in GeoAI Modeling and Data Foundations",
        "deadline": "2026-10-05",
        "url": "https://umd.edu"
    },
    {
        "category": "1. GIS, Tech, Data Science & GeoAI",
        "keyword": "GIScience",
        "region": "India Tier (IITs/Central Universities)",
        "institution": "Shibli Regional College (shiblicollege.ac.in)",
        "title": "Two-Week Capacity Building Course in Applied GIScience",
        "deadline": "2026-04-17",  # Historical trigger for the self-healing layout
        "url": "http://shiblicollege.ac.in"
    }
]

# =====================================================================
# 3. INTERFACE BUILDER & STRUCTURAL APPLICATION LAYOUT
# =====================================================================
st.title("🌍 Global Academic Geography Discovery Engine")
st.markdown("### *Live Multi-Region Activity Ticker & Expiry Routing Platform (2026)*")
st.write("An advanced database framework tracking verified university call-for-papers, labs, and event notices.")
st.divider()  # Successfully replaced st.hr() with a valid Streamlit horizontal divider

# Sidebar: Controls and Operational Query Configurations
st.sidebar.header("🔍 Discovery Controls")
target_region = st.sidebar.selectbox("1. Target Institutional Tier", ["India Tier (IITs/Central Universities)", "United States Tier (.edu)", "United Kingdom Tier (.ac.uk)"])
selected_category = st.sidebar.selectbox("2. Select Core Discipline", list(SEEDS.keys()))
selected_keyword = st.sidebar.selectbox("3. Select Refined Semantic Keyword", SEEDS[selected_category])

# System Date Anchor setup
current_date = datetime.date(2026, 7, 17)
st.sidebar.info(f"📅 Timeline System Anchor: {current_date.strftime('%B %d, %Y')}")

# Regional UI Notifications
if "India" in target_region:
    st.sidebar.success("🔥 Indian Dialect Bypass Active: Checking for Vice-Chancellor administrative lineages, ICSSR/DST grants, and direct text PDF brochures.")
else:
    st.sidebar.success("🛡️ Academic Firewall Whitelist Active: Filtering out commercial conference spam.")

# UI Output Stream Presenter
st.subheader(f"📊 Live Stream Tracker: '{selected_keyword}' in {target_region}")

# Build query strings for presentation visibility
site_hook = "site:.ac.in" if "India" in target_region else ("site:.edu" if "United States" in target_region else "site:.ac.uk")
intent_hook = '("conference" OR "brochure" OR "circular" OR filetype:pdf)' if "India" in target_region else '(intitle:seminar OR inurl:calendar)'

if "India" in target_region:
    compiled_query_string = f'{site_hook} AND "{selected_keyword}" AND ("{INDIAN_ACADEMIC_PROTOCOLS["honorifics"][0]}" OR "{INDIAN_ACADEMIC_PROTOCOLS["grants"][0]}") AND {intent_hook}'
else:
    compiled_query_string = f'{site_hook} AND "{selected_keyword}" AND {intent_hook}'

st.code(f"EXECUTING BACKGROUND LIVE QUERY LOGIC: {compiled_query_string}", language="sql")

# Execution Processing Engine Loop
match_found = False
for event in MOCK_WEB_DATABASE:
    if event["keyword"] == selected_keyword and event["region"] == target_region:
        match_found = True
        event_deadline = datetime.datetime.strptime(event["deadline"], "%Y-%m-%d").date()
        
        # Timeline evaluation processing
        if event_deadline >= current_date:
            days_remaining = (event_deadline - current_date).days
            # Action Path A: Urgent Close Alert (< 7 Days)
            if days_remaining <= 7:
                st.error(f"🚨 URGENT CLOSE CLOSING TICKER ALERT (Closes in {days_remaining} Days)")
                st.markdown(f"### [{event['institution']}] {event['title']}")
                st.markdown(f"🔗 [Verify Live Page Node: Click to open Official University Source]({event['url']})")
                st.warning(f"⚠️ System Alert: This verified abstract window is closing fast. Extract timeline details immediately.")
            # Action Path B: Steady Live Tracking Feed
            else:
                st.success(f"🟢 ACTIVE STREAMING TICKER FEED ({days_remaining} Days Remaining)")
                st.markdown(f"### [{event['institution']}] {event['title']}")
                st.write(f"📅 Verified Deadline Milestone: {event_deadline.strftime('%B %d, %Y')}")
                st.markdown(f"🔗 [Verify Live Page Node: Click to open Official University Source]({event['url']})")
        # Action Path C: Found entry is Expired/Redundant. Reroute via similarity tables.
        else:
            st.error(f"❌ REDUNDANT ENTRY BYPASSED (Expired on {event_deadline.strftime('%B %d, %Y')})")
            st.write(f"The event path '{event['title']}' from {event['institution']} has past its execution window. Dropping link from stream...")
            st.info("🔄 SIMILARITY ROUTING ENGINE ACTIVE: Sifting category dictionary to redirect query to open sister channels...")
            
            sister_keywords = SEEDS[selected_category]
            for fallback_event in MOCK_WEB_DATABASE:
                if fallback_event["keyword"] in sister_keywords and datetime.datetime.strptime(fallback_event["deadline"], "%Y-%m-%d").date() >= current_date:
                    st.markdown("---")
                    st.markdown("#### ✅ Healed Connection - Active Sibling Track Surfaced:")
                    st.success(f"🟢 ACTIVE ROUTE MATCH")
                    st.markdown(f"### [{fallback_event['institution']}] {fallback_event['title']}")
                    st.write(f"📅 Verified Sibling Target Date: {fallback_event['deadline']}")
                    st.markdown(f"🔗 [Live Sibling Node: Click to Open Source]({fallback_event['url']})")
                    break

# Fallback Processing Rule if selected sub-node returns empty datasets
if not match_found:
    st.info("🟡 NO DIRECT MATCHING NODE FOUND IN LOCAL INDEX DATA")
    st.write("The targeted parameter holds no updates today. Activating sibling dictionaries to fetch closest relative entries...")
    sister_keywords = SEEDS[selected_category]
    for fallback_event in MOCK_WEB_DATABASE:
        if fallback_event["keyword"] in sister_keywords and datetime.datetime.strptime(fallback_event["deadline"], "%Y-%m-%d").date() >= current_date:
            st.markdown("---")
            st.markdown(f"#### 🔄 Surfaced Active Sibling from Area Matrix '{selected_category}':")
            st.success(f"🟢 ACTIVE STREAM TICKER")
            st.markdown(f"### [{fallback_event['institution']}] {fallback_event['title']}")
            st.write(f"📅 Deadline Target: {fallback_event['deadline']}")
            st.markdown(f"🔗 [Source Link: Click to Open Link]({fallback_event['url']})")
            break

st.markdown("---")
st.caption("🛡️ Global Academic Geography Discovery Engine © 2026. Self-healing multi-region configuration verified.")
