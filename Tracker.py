import streamlit as st
import pandas as pd
import datetime
import os

# =====================================================================
# CORE ENGINE LAYER & INTERFACE CONFIGURATIONS
# =====================================================================
st.set_page_config(
    page_title="Critical Geography & Radical Humanities Engine", 
    page_icon="✊🏽", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Academic UI Theme - Ultra High Contrast
st.markdown("""
    <style>
    .main .block-container { padding-top: 1.5rem; padding-bottom: 1.5rem; }
    h1 { font-weight: 800; color: #7F1D1D; letter-spacing: -0.5px; }
    h3 { font-weight: 700; color: #1E293B; margin-top: 1.5rem; }
    .univ-card {
        background-color: #FAFAFA;
        padding: 18px 22px;
        border-radius: 8px;
        border-left: 6px solid #7F1D1D;
        border-top: 1px solid #94A3B8;
        border-right: 1px solid #94A3B8;
        border-bottom: 1px solid #94A3B8;
        margin-bottom: 12px;
    }
    .univ-card h4 {
        color: #0F172A !important;
        font-weight: 800;
        margin-top: 0px;
        margin-bottom: 6px;
        font-size: 1.25rem;
    }
    .meta-text {
        color: #334155 !important;
        font-size: 14px;
        font-weight: 500;
    }
    code {
        color: #B91C1C;
        background-color: #FEF2F2;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: monospace;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Dynamic Temporal Constraint Engine
current_date = datetime.date.today()
CURRENT_YEAR = current_date.year
NEXT_YEAR = CURRENT_YEAR + 1

ALL_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
current_month_idx = current_date.month - 1
remaining_months = ALL_MONTHS[current_month_idx:]

month_queries = " OR ".join([f'"{m} {CURRENT_YEAR}"' for m in remaining_months])
STRICT_TEMPORAL = f'("upcoming" OR "{NEXT_YEAR}" OR {month_queries})'
BROAD_TEMPORAL = f'("{CURRENT_YEAR}" OR "{NEXT_YEAR}" OR "upcoming")'

st.title("✊🏽 Critical Geography & Radical Humanities Engine")
st.markdown("##### Dual-Mode Portal Tracking Across National Research Intensities, Departmental Fe feeds, and Funding Matrices")
st.markdown("---")

# =====================================================================
# UGC REGISTERED MASTER DATABASE INGESTION
# =====================================================================
@st.cache_data
def load_base_registry():
    file_name = "Welcome to UGC, New Delhi, India.csv"
    if os.path.exists(file_name):
        try:
            data = pd.read_csv(file_name)
            data.columns = [c.strip() for c in data.columns]
            data['Name of the University'] = data['Name of the University'].astype(str).str.strip()
            data['state'] = data['state'].astype(str).str.strip()
            data['Address'] = data['Address'].fillna('').astype(str).str.strip()
            return data, True
        except Exception as e:
            return None, f"Registry Ingestion Failure: {str(e)}"
    return None, False

df, success = load_base_registry()

if not success:
    st.error("🚨 CRITICAL DISRUPTION: Master database file 'Welcome to UGC, New Delhi, India.csv' not found.")
    st.stop()

# =====================================================================
# SIDEBAR CONFIGURATORS (Natively Tied Variables)
# =====================================================================
st.sidebar.markdown("### 🗺️ Territorial Scope")
state_list = sorted(df['state'].unique().tolist())
default_state_idx = state_list.index("Madhya Pradesh") if "Madhya Pradesh" in state_list else 0
selected_state = st.sidebar.selectbox("Target Regional Node", state_list, index=default_state_idx)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📂 Structural Document Pattern")
RESOURCE_TYPES = {
    "Conferences, Seminars & Symposia": "(conference OR seminar OR symposium OR \"call for papers\" OR registration)",
    "Methodology Workshops & Training": "(\"methodology workshop\" OR \"capacity building\" OR FDP OR \"research methodology\")",
    "Brochures & Notification PDFs": "(filetype:pdf OR brochure OR circular OR \"notice board\")"
}
chosen_resource = st.sidebar.selectbox("Target Output Format", list(RESOURCE_TYPES.keys()))
resource_query = RESOURCE_TYPES[chosen_resource]

# =====================================================================
# RE-ENGINEERED DORK COMPILER PIPELINE (Directly Binds Selected Options)
# =====================================================================
def compile_dork(institution_name, target_dept_string=None, mode="strict"):
    base_identity = f'"{institution_name}"'
    dept_fallback = '("Geography" OR "Social Sciences" OR "Humanities" OR "Development Studies")'
    active_dept = target_dept_string if target_dept_string else dept_fallback
    
    if mode == "strict":
        dork_string = f"{base_identity} AND {active_dept} AND {resource_query} AND {STRICT_TEMPORAL}"
    else:
        dork_string = f"{base_identity} AND {resource_query} AND {BROAD_TEMPORAL}"
        
    return f"https://www.google.com/search?q={dork_string.replace(' ', '+')}"

# =====================================================================
# REORDERED MASTER RESEARCH HUBS ARRAY (Geography -> CSDS -> IITs)
# =====================================================================
TOP_50_HUMANITIES_GEOGRAPHY = [
    # --- PHASE 1: POPULAR GEOGRAPHY DEPARTMENTS ---
    {"name": "Jawaharlal Nehru University (CSRD)", "type": "Pure Geography Focus / Regional Development", "dept": '("Centre for the Study of Regional Development" OR "CSRD" OR "Geography")', "feed_path": "https://www.jnu.ac.in/events"},
    {"name": "Delhi School of Economics", "type": "Pure Geography Focus", "dept": '("Department of Geography" OR "DSE" OR "Delhi University")', "feed_path": "https://www.du.ac.in"},
    {"name": "Aligarh Muslim University", "type": "Pure Geography Focus", "dept": '("Department of Geography" OR "AMU")', "feed_path": "https://www.amu.ac.in"},
    {"name": "Banaras Hindu University", "type": "Pure Geography Focus", "dept": '("Department of Geography" OR "BHU")', "feed_path": "https://bhu.ac.in"},
    {"name": "Jamia Millia Islamia", "type": "Pure Geography Focus", "dept": '("Department of Geography" OR "JMI")', "feed_path": "https://www.jmi.ac.in"},
    {"name": "Panjab University", "type": "Pure Geography Focus", "dept": '("Department of Geography")', "feed_path": "https://puchd.ac.in"},
    {"name": "University of Calcutta", "type": "Pure Geography Focus", "dept": '("Department of Geography")', "feed_path": "https://www.caluniv.ac.in"},
    {"name": "University of Madras", "type": "Pure Geography Focus", "dept": '("Department of Geography")', "feed_path": "https://www.unom.ac.in"},
    {"name": "Savitribai Phule Pune University", "type": "Pure Geography Focus", "dept": '("Department of Geography")', "feed_path": "http://www.unipune.ac.in"},
    {"name": "Osmania University", "type": "Pure Geography Focus", "dept": '("Department of Geography")', "feed_path": "https://www.osmania.ac.in"},
    {"name": "University of Allahabad", "type": "Pure Geography Focus", "dept": '("Department of Geography")', "feed_path": "https://allduniv.ac.in"},
    {"name": "Dr. Harisingh Gour Vishwavidyalaya", "type": "Regional & Rural Development Node", "dept": '("School of Studies in Geography" OR "SoS in Geography")', "feed_path": "http://www.dhsgsu.edu.in"},
    {"name": "Vikram University", "type": "Regional & Rural Development Node", "dept": '("School of Studies in Geography")', "feed_path": "http://www.vikramuniv.ac.in"},
    {"name": "Barkatullah University", "type": "Regional & Rural Development Node", "dept": '("Department of Geography")', "feed_path": "http://www.bubhopal.ac.in"},
    {"name": "Rani Durgavati Vishwavidyalaya", "type": "Regional & Rural Development Node", "dept": '("Department of Geography")', "feed_path": "http://www.rdunijbpin.org"},
    {"name": "Central University of Punjab", "type": "Pure Geography Focus", "dept": '("Department of Geography")', "feed_path": "https://cup.edu.in"},

    # --- PHASE 2: CSDS & SPECIALIZED SOCIAL SCIENCE NODES ---
    {"name": "Centre for the Study of Developing Societies (CSDS)", "type": "Elite Radical Humanities Node", "dept": '("CSDS" OR "Social and Political Theory" OR "Lokniti")', "feed_path": "https://www.csds.in"},
    {"name": "Indian Institute for Human Settlements (IIHS)", "type": "Elite Spatial & Transition Node", "dept": '("IIHS" OR "Urban ARC" OR "Geospatial Lab")', "feed_path": "https://iihs.co.in"},
    {"name": "Tata Institute of Social Sciences", "type": "Specialized Intersectionality Hub", "dept": '("School of Rural Development" OR "TISS")', "feed_path": "https://tiss.edu"},
    {"name": "Giri Institute of Development Studies", "type": "Specialized Policy / Margin Tracking", "dept": '("GIDS")', "feed_path": "http://gids.org.in"},
    {"name": "Institute of Economic Growth", "type": "Specialized Policy / Margin Tracking", "dept": '("IEG")', "feed_path": "https://www.iegindia.org"},
    {"name": "Centre for Development Studies", "type": "Specialized Policy / Margin Tracking", "dept": '("CDS")', "feed_path": "https://cds.edu"},
    {"name": "National Institute of Rural Development", "type": "Dedicated Rural Development Node", "dept": '("NIRDPR")', "feed_path": "http://nirdpr.org.in"},
    {"name": "Institute of Rural Management Anand", "type": "Dedicated Rural Development Node", "dept": '("IRMA")', "feed_path": "https://irma.ac.in"},
    {"name": "Centre for Policy Research", "type": "Specialized Policy / Margin Tracking", "dept": '("CPR")', "feed_path": "https://cprindia.org"},
    {"name": "Madras Institute of Development Studies", "type": "Specialized Policy / Margin Tracking", "dept": '("MIDS")', "feed_path": "https://www.mids.ac.in"},

    # --- PHASE 3: IITS & COMPUTATIONAL LABS ---
    {"name": "IIT Delhi (HSS Department)", "type": "Premium Tech-Humanities Node", "dept": '("Department of Humanities and Social Sciences" OR "IITD HSS")', "feed_path": "https://hss.iitd.ac.in"},
    {"name": "IIT Bombay (HSS / CSRE)", "type": "Premium Tech-Humanities Node", "dept": '("Humanities and Social Sciences" OR "CSRE")', "feed_path": "https://www.iitb.ac.in"},
    {"name": "IIT Gandhinagar (HSS Department)", "type": "Premium Tech-Humanities Node", "dept": '("Humanities and Social Sciences" OR "IITGN HSS")', "feed_path": "https://hss.iitgn.ac.in"},
    {"name": "IIT Madras (HSS Department)", "type": "Premium Tech-Humanities Node", "dept": '("Humanities and Social Sciences" OR "IITM HSS")', "feed_path": "https://hss.iitm.ac.in"},
    {"name": "IIIT Hyderabad (HSRC / Spatial Labs)", "type": "Computational-Humanities Intersection", "dept": '("Human Sciences Research Centre" OR "HSRC" OR "Lab for Spatial Informatics")', "feed_path": "https://hsrc.iiit.ac.in"},
    {"name": "IIT Kanpur", "type": "Spatial Sciences & GIS Hub", "dept": '("Humanities and Social Sciences" OR "HSS" OR "Geoinformatics")', "feed_path": "https://www.iitk.ac.in"},
    {"name": "IIT Kharagpur", "type": "Spatial Sciences & GIS Hub", "dept": '("Humanities and Social Sciences" OR "HSS")', "feed_path": "https://www.iitkgp.ac.in"}
]

# =====================================================================
# GLOBAL FUNDER SWEEP (CROSS-COUNTRY MATRIX SCANNER)
# =====================================================================
st.subheader("🌐 Global Funder Sweep (Cross-Country Matrix Scan)")
st.markdown(f"**Current Structural Filter Selection:** `{chosen_resource}`")

col_sweep1, col_sweep2 = st.columns(2)

with col_sweep1:
    cbp_domains = '(site:ac.in OR site:res.in OR site:org.in OR site:edu OR site:gov.in)'
    cbp_dork = f'{cbp_domains} "Capacity Building" AND "ICSSR" AND {STRICT_TEMPORAL}'
    cbp_url = f"https://www.google.com/search?q={cbp_dork.replace(' ', '+')}"
    st.info("🎯 **Capacity Building Programmes (CBP)**")
    st.link_button("🚀 Launch Country-Wide CBP Sweep", cbp_url, use_container_width=True)

with col_sweep2:
    rmw_dork = f'{cbp_domains} "Research Methodology" AND ("Workshop" OR "FDP") AND "ICSSR" AND {STRICT_TEMPORAL}'
    rmw_url = f"https://www.google.com/search?q={rmw_dork.replace(' ', '+')}"
    st.info("📊 **Research Methodology Workshops (RMW)**")
    st.link_button("🚀 Launch Country-Wide RMW Sweep", rmw_url, use_container_width=True)

st.markdown("---")

# =====================================================================
# DISPLAY ZONE 1: REORDERED NATIONAL NETWORK
# =====================================================================
st.subheader("🔥 Core Research Intensities (National Elite Nodes)")
st.markdown(f"Direct structural search keys automatically modified to match the pattern filter selection: `{chosen_resource}`")

for idx, item in enumerate(TOP_50_HUMANITIES_GEOGRAPHY):
    with st.container():
        st.markdown(f"""
        <div class="univ-card">
            <h4>🏫 {item['name']}</h4>
            <p class="meta-text">
                <strong>Structural Profile:</strong> {item['type']} | <strong>Active Tracking Logic:</strong> <code>{item['dept']}</code>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_action1, col_action2, col_action3 = st.columns([1, 1.3, 1.3])
        with col_action1:
            st.link_button("🌐 Open Portal", item['feed_path'], use_container_width=True, key=f"feed_portal_{idx}")
        with col_action2:
            st.link_button("🔎 Strict Deep Dork", compile_dork(item['name'], target_dept_string=item['dept'], mode="strict"), use_container_width=True, key=f"strict_dork_{idx}")
        with col_action3:
            st.link_button("🔓 Broad Safety Scan", compile_dork(item['name'], target_dept_string=item['dept'], mode="broad"), use_container_width=True, key=f"broad_dork_{idx}")
        st.markdown("<br>", unsafe_allow_html=True)

# =====================================================================
# DISPLAY ZONE 2: TERRITORIAL HUB COMPLETE INDEX (Reactive Loop)
# =====================================================================
st.markdown("---")
filtered_state_df = df[df['state'] == selected_state].sort_values(by='Name of the University')

st.subheader(f"🏛️ Territorial Registry Landscape Node: {selected_state} ({len(filtered_state_df)} Registered Base Nodes Found)")

if not filtered_state_df.empty:
    for idx, row in filtered_state_df.iterrows():
        univ_name = row['Name of the University']
        
        with st.container():
            st.markdown(f"**🏛️ {univ_name}**  \n📍 `Registry Address String:` {row['Address']}")
            
            col_state_btn1, col_state_btn2 = st.columns([1, 1])
            with col_state_btn1:
                st.link_button("🔎 Run Strict Scan", compile_dork(univ_name, mode="strict"), use_container_width=True, key=f"state_strict_{idx}")
            with col_state_btn2:
                st.link_button("🔓 Run Broad Safety Scan", compile_dork(univ_name, mode="broad"), use_container_width=True, key=f"state_broad_{idx}")
            st.markdown("---")
else:
    st.warning(f"No database entries matches the chosen target selection: {selected_state}")
