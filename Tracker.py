import streamlit as st
import pandas as pd
import datetime
import os

# Page Configuration
st.set_page_config(
    page_title="Specialized Geography & Policy Resource Tracker", 
    page_icon="🌍", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Clean CSS (Protects Streamlit's native state reactivity)
st.markdown("""
    <style>
    .main .block-container { padding-top: 1.5rem; padding-bottom: 1.5rem; }
    h1 { font-weight: 800; color: #1E3A8A; }
    .card-box {
        background-color: #F8FAFC;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        margin-bottom: 8px;
    }
    .powerhouse-badge {
        background-color: #F0FDF4; color: #166534;
        padding: 4px 10px; border-radius: 6px; font-weight: 600; font-size: 12px;
        border: 1px solid #BBF7D0;
    }
    .standard-badge {
        background-color: #F1F5F9; color: #475569;
        padding: 4px 10px; border-radius: 6px; font-weight: 500; font-size: 12px;
        border: 1px solid #CBD5E1;
    }
    </style>
""", unsafe_allow_html=True)

# Automated Current Year System (2026 Context)
CURRENT_YEAR = datetime.datetime.now().year
ACADEMIC_SESSION_QUERY = f"({CURRENT_YEAR} OR {CURRENT_YEAR}-{str(CURRENT_YEAR+1)[2:]})"

st.title("🌍 Specialized Geography & Policy CFP Discovery Engine")
st.markdown("##### Targeted Query Routing for Pure Geography Departments & Specialized Regional Research Hubs")
st.markdown("---")

# =====================================================================
# DATA INGESTION & DEPARTAMENTAL TARGETING INDEX
# =====================================================================
@st.cache_data
def load_and_tier_departments():
    file_name = "Welcome to UGC, New Delhi, India.csv"
    if os.path.exists(file_name):
        try:
            data = pd.read_csv(file_name)
            data.columns = [c.strip() for c in data.columns]
            data['Name of the University'] = data['Name of the University'].astype(str).str.strip()
            data['state'] = data['state'].astype(str).str.strip()
            data['Address'] = data['Address'].fillna('').astype(str).str.strip()
            
            # PURE GEOGRAPHY & SPECIALIZED REGIONAL RESEARCH DEPARTMENTS INDEX
            GEOGRAPHY_HUBS = [
                "Aligarh Muslim University", 
                "Banaras Hindu University", 
                "Jawaharlal Nehru University", 
                "University of Delhi",
                "Jamia Millia Islamia",
                "Panjab University",
                "University of Madras",
                "University of Calcutta",
                "Dr. Harisingh Gour Vishwavidyalaya", 
                "Barkatullah University"
            ]
            
            def identify_departmental_strength(name):
                for hub in GEOGRAPHY_HUBS:
                    if hub.lower() in name.lower():
                        return 1  # Tier 1: Powerhouse
                return 2      # Tier 2: Standard
                
            data['Dept_Tier'] = data['Name of the University'].apply(identify_departmental_strength)
            return data, True
        except Exception as e:
            return None, f"Registry Parsing Error: {str(e)}"
    return None, False

df, success = load_and_tier_departments()

if not success:
    st.error("🚨 Master database file 'Welcome to UGC, New Delhi, India.csv' not found.")
    st.stop()

# =====================================================================
# REACTIVE SIDEBAR CONTROLS
# =====================================================================
st.sidebar.markdown("### 🗺️ Territorial Filter")
state_list = sorted(df['state'].unique().tolist())
default_state_idx = state_list.index("Madhya Pradesh") if "Madhya Pradesh" in state_list else 0
selected_state = st.sidebar.selectbox("Target Regional Registry Node", state_list, index=default_state_idx)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏛️ Targeted Academic Unit")
DEPT_FILTERS = {
    "Isolate Pure Geography Departments": '("Department of Geography" OR "Dept of Geography" OR "Geographer")',
    "Isolate Specialized Policy/Development Centers": '("Center for Regional Development" OR "Department of Education" OR "Social Sciences")',
    "Search General Institutional Notices": ''
}
chosen_unit = st.sidebar.selectbox("Academic Unit Focus", list(DEPT_FILTERS.keys()))

st.sidebar.markdown("---")
st.sidebar.markdown("### 📂 Upload Format Hack")
RESOURCE_TYPES = {
    "Brochures & Notification PDFs": "(filetype:pdf OR brochure OR circular OR \"notice board\")",
    "Conferences & Seminars": "(national conference OR seminar OR symposium OR registration)",
    "Workshops & Methodology Training": "(methodology workshop OR capacity building OR FDP)",
    "Journal Special Issues & Chapters": "(\"call for chapters\" OR \"special issue\" OR peer reviewed)"
}
chosen_resource = st.sidebar.selectbox("Resource Assets Target", list(RESOURCE_TYPES.keys()))

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 Core Deep Research Domains")
DOMAIN_MAPPING = {
    "Rural Evolution & Historical Geography": "(\"Rural Evolution\" OR \"Historical Geography\" OR \"Village Definitions\" OR \"Rural Transformation\" OR \"Spatial Evolution\")",
    "Educational Disparities & School Infrastructure": "(\"Educational Disparities\" OR \"School Infrastructure\" OR \"Literacy Rates\" OR \"Enrolment Trends\" OR \"District Disparities\")",
    "Ancient Astronomy vs. Standard Time": "(\"Meridian of Ujjain\" OR \"Standard Time\" OR \"Astronomical Canons\" OR \"Time Calculation\" OR \"Prime Meridian\")",
    "Government Schemes & Development Policy": "(\"Mera Gaon Mera Dharohar\" OR \"Smart Village\" OR \"Development Policy\" OR \"Rural Schemes\")"
}
chosen_domain = st.sidebar.selectbox("Isolate Research Focus", list(DOMAIN_MAPPING.keys()))

st.sidebar.markdown("---")
st.sidebar.markdown("### 📍 Micro-Locality Boundary")
specific_district = st.sidebar.text_input("Add Specific District Filter (Optional)", placeholder="e.g., Alirajpur, Jhabua, Barwani")

# =====================================================================
# CONDITIONAL FILTERING PIPELINE (POWERHOUSE VS ALL)
# =====================================================================
# Filter by state first
state_df = df[df['state'] == selected_state].copy()

# Split the dataset dynamically
powerhouse_df = state_df[state_df['Dept_Tier'] == 1].sort_values(by='Name of the University')
standard_df = state_df[state_df['Dept_Tier'] == 2].sort_values(by='Name of the University')

# =====================================================================
# INTERFACE DISPLAY
# =====================================================================
col_m1, col_m2 = st.columns(2)
col_m1.metric("Geography Powerhouses in State", len(powerhouse_df))
col_m2.metric("Other Regional Hubs Available", len(standard_df))

st.markdown("---")

# Shared search string generators
unit_string = DEPT_FILTERS[chosen_unit]
resource_query = RESOURCE_TYPES[chosen_resource]
domain_query = DOMAIN_MAPPING[chosen_domain]

def build_search_url(univ_name):
    ind_parts = [f'"{univ_name}"']
    if unit_string:
        ind_parts.append(unit_string)
    ind_parts.append(resource_query)
    ind_parts.append(domain_query)
    if specific_district:
        ind_parts.append(f'"{specific_district}"')
    ind_parts.append(ACADEMIC_SESSION_QUERY)
    
    ind_search = " AND ".join(ind_parts)
    return f"https://www.google.com/search?q={ind_search.replace(' ', '+')}"

# RENDER ZONE 1: PRIMARY GEOGRAPHY POWERHOUSES
st.markdown("### 🔥 Primary Targets: Geography & Regional Policy Powerhouses")
st.markdown("These institutions contain specific, high-yield departmental infrastructure for your fields.")

if not powerhouse_df.empty:
    for idx, row in powerhouse_df.iterrows():
        univ_name = row['Name of the University']
        st.markdown(f"""
            <div class="card-box">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="font-size: 16px; font-weight: 700; color: #166534;">🌟 {univ_name}</span><br>
                        <span style="font-size: 13px; color: #64748B;">📍 Location: {row['Address']}</span>
                    </div>
                    <div>
                        <span class="powerhouse-badge">🌍 Pure Dept / Specialized Center</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        c_space, c_btn = st.columns([5, 1])
        with c_btn:
            st.link_button("🔎 Scan Powerhouse", build_search_url(univ_name), use_container_width=True, key=f"pwr_{idx}")
        st.markdown("<br>", unsafe_allow_html=True)
else:
    st.info("No primary Geography/Policy powerhouses explicitly tracked in this state's registry yet. You can scan the broader institutional list below.")

st.markdown("---")

# RENDER ZONE 2: DYNAMIC REGISTRY TOGGLE ("CHECK OTHER UNIVERSITIES")
st.markdown("### 🏛️ Secondary Targets: Comprehensive State Registry")
show_all = st.checkbox("Show remaining state universities to expand my search options", value=False)

if show_all:
    if not standard_df.empty:
        st.markdown("---")
        for idx, row in standard_df.iterrows():
            univ_name = row['Name of the University']
            st.markdown(f"""
                <div class="card-box">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span style="font-size: 15px; font-weight: 600; color: #334155;">🏛️ {univ_name}</span><br>
                            <span style="font-size: 13px; color: #64748B;">📍 Location: {row['Address']}</span>
                        </div>
                        <div>
                            <span class="standard-badge">General Registry Hub</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            c_space, c_btn = st.columns([5, 1])
            with c_btn:
                st.link_button("🔎 Scan Hub", build_search_url(univ_name), use_container_width=True, key=f"std_{idx}")
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.warning("No secondary general universities found for this state selection.")
