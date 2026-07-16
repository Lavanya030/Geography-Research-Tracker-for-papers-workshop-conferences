import streamlit as st

# Set up page configurations at the absolute top
st.set_page_config(page_title="Global Geography Hub", page_icon="🌍", layout="wide")

# =====================================================================
# 1. CURATED DATABASE OF LEGITIMATE GEOGRAPHY DEPARTMENTS, LABS & GROUPS
# =====================================================================
INSTITUTIONAL_DIRECTORY = [
    # --- INDIA TIER ---
    {
        "name": "Centre for the Study of Regional Development (CSRD)",
        "parent": "Jawaharlal Nehru University (JNU)",
        "region": "India",
        "focus": "Human, Rural, Class & Regional Development",
        "description": "One of India's premier centers focusing on spatial inequalities, rural development, agrarian changes, and socio-economic marginalization.",
        "homepage": "https://www.jnu.ac.in/sss/csrd",
        "events_page": "https://www.jnu.ac.in/seminars-and-conferences",
        "notes": "Highly relevant for ICSSR-sponsored capacity building, national seminars, and rural development circulars."
    },
    {
        "name": "Department of Geography, Delhi School of Economics",
        "parent": "University of Delhi",
        "region": "India",
        "focus": "Human, Rural, Class & Regional Development",
        "description": "A historic hub for spatial theory, agricultural geography, and environmental development studies in India.",
        "homepage": "http://geography.du.ac.in/",
        "events_page": "http://geography.du.ac.in/seminars.html",
        "notes": "Regularly hosts national-level workshops, geography congresses, and guest lecture series."
    },
    {
        "name": "Department of Humanities and Social Sciences (HSS)",
        "parent": "IIT Bombay",
        "region": "India",
        "focus": "Interdisciplinary Social Sciences & Tech",
        "description": "Hosts specialized research in developmental planning, socio-spatial transformations, and policy-based geography research.",
        "homepage": "https://www.hss.iitb.ac.in/",
        "events_page": "https://www.hss.iitb.ac.in/en/events-list",
        "notes": "Good source for highly-funded interdisciplinary symposiums and methodology workshops."
    },
    {
        "name": "Department of Geography and Geoinformatics",
        "parent": "Royal Global University",
        "region": "India",
        "focus": "GIS, Tech, Data Science & GeoAI",
        "description": "Blends classic physical and human geography with modern remote sensing and GIS frameworks.",
        "homepage": "https://www.rgu.ac/department-geography-geoinformatics",
        "events_page": "https://www.rgu.ac/department-geography-geoinformatics",
        "notes": "Regularly runs field studies, invited talks, and regional developmental panels."
    },
    
    # --- UNITED KINGDOM TIER ---
    {
        "name": "Geographic Data Science Lab (GDSL)",
        "parent": "University of Liverpool",
        "region": "United Kingdom",
        "focus": "GIS, Tech, Data Science & GeoAI",
        "description": "A world-leading center pioneering new methods in spatial analytics, machine learning, and data integration.",
        "homepage": "https://www.liverpool.ac.uk/geographic-data-science/",
        "events_page": "https://www.liverpool.ac.uk/geographic-data-science/news-and-events/",
        "notes": "The primary spot for cutting-edge GIScience, spatial data science bootcamps, and GeoAI workshops."
    },
    {
        "name": "Environmental Change Institute (ECI)",
        "parent": "University of Oxford",
        "region": "United Kingdom",
        "focus": "Physical Landscapes & Environmental Governance",
        "description": "Organizes interdisciplinary research on climate change, energy transitions, ecosystems, and food security.",
        "homepage": "https://www.eci.ox.ac.uk/",
        "events_page": "https://www.eci.ox.ac.uk/events",
        "notes": "Hosts globally influential seminars, international conferences, and climate workshops."
    },
    {
        "name": "School of Geography and Environmental Science",
        "parent": "University of Southampton",
        "region": "United Kingdom",
        "focus": "Interdisciplinary Social Sciences & Tech",
        "description": "Leading research hub in population mapping (WorldPop), environmental processes, and geospatial computing.",
        "homepage": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-geography-and-environmental-science",
        "events_page": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-geography-and-environmental-science#news_and_events",
        "notes": "Excellent resource for geospatial computing workshops and global health geography updates."
    },

    # --- UNITED STATES TIER ---
    {
        "name": "Graduate School of Geography",
        "parent": "Clark University",
        "region": "United States",
        "focus": "Human, Rural, Class & Regional Development",
        "description": "Renowned for pioneering critical geography, feminist geopolitics, urban-environmental studies, and political ecology.",
        "homepage": "https://www.clarku.edu/departments/geography/",
        "events_page": "https://www.clarku.edu/departments/geography/news-events/",
        "notes": "A historic pillar of radical, human, and developmental geography."
    },
    {
        "name": "Center for Geospatial Information Science (CGIS)",
        "parent": "University of Maryland",
        "region": "United States",
        "focus": "GIS, Tech, Data Science & GeoAI",
        "description": "Highly active research lab focusing on Spatial Computing, GeoAI, Remote Sensing, and spatial database modeling.",
        "homepage": "https://www.geog.umd.edu/landingtopic/cgis",
        "events_page": "https://geog.umd.edu/events",
        "notes": "Hosts regular plenary panels, technical workshops, and UCGIS symposium activities."
    }
]

# =====================================================================
# 2. APPLICATION LAYOUT & ROUTING
# =====================================================================
st.title("🌍 Global Academic Geography Discovery Hub")
st.markdown("### *Verifiable Notice Boards, Active Labs & Institutional Event Trackers*")
st.write("A clean, focused directory mapping legitimate academic geography spaces. No commercial aggregators—just direct, official university sources.")
st.divider()

# Sidebar Filters
st.sidebar.header("🎯 Filter Directories")
selected_region = st.sidebar.multiselect(
    "1. Select Regional Scope", 
    options=["India", "United Kingdom", "United States"], 
    default=["India", "United Kingdom", "United States"]
)

selected_focus = st.sidebar.multiselect(
    "2. Select Academic Focus",
    options=[
        "GIS, Tech, Data Science & GeoAI",
        "Human, Rural, Class & Regional Development",
        "Physical Landscapes & Environmental Governance",
        "Interdisciplinary Social Sciences & Tech"
    ],
    default=[
        "GIS, Tech, Data Science & GeoAI",
        "Human, Rural, Class & Regional Development",
        "Physical Landscapes & Environmental Governance",
        "Interdisciplinary Social Sciences & Tech"
    ]
)

# Filter Logic
filtered_directory = [
    item for item in INSTITUTIONAL_DIRECTORY 
    if item["region"] in selected_region and item["focus"] in selected_focus
]

# Display Statistics
st.markdown(f"Showing **{len(filtered_directory)} verified nodes** out of {len(INSTITUTIONAL_DIRECTORY)} total recorded institutions.")

# =====================================================================
# 3. DIRECTORY LAYOUT
# =====================================================================
if filtered_directory:
    for idx, item in enumerate(filtered_directory):
        # Create a container box for each verified institution
        with st.container():
            col_info, col_action = st.columns([3, 1], gap="medium")
            
            with col_info:
                st.markdown(f"### {idx+1}. {item['name']}")
                st.markdown(f"**Parent Institution:** `{item['parent']}` | **Region:** `{item['region']}`")
                st.markdown(f"**Disciplinary Focus Area:** `{item['focus']}`")
                st.write(item["description"])
                
                # Highlight Notes / Tips for scholars
                st.caption(f"💡 **Why Monitor This:** {item['notes']}")
                
            with col_action:
                st.write("")  # Padding
                st.write("")
                # Direct links to verified portals
                st.link_button("🌐 Visit Lab Homepage", item["homepage"], use_container_width=True)
                st.link_button("📅 Trace Events & Notices", item["events_page"], type="primary", use_container_width=True)
            
            st.divider()
else:
    st.warning("No verified academic institutions match your selected filters. Try broadening your selection in the sidebar.")

st.sidebar.markdown("---")
st.sidebar.caption("🛡️ Global Academic Geography Discovery Hub © 2026. This layout bypasses commercial noise to provide direct paths to primary notices.")
