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

# Deep Academic UI Theme
st.markdown("""
    <style>
    .main .block-container { padding-top: 1.5rem; padding-bottom: 1.5rem; }
    h1 { font-weight: 800; color: #7F1D1D; letter-spacing: -0.5px; }
    h3 { font-weight: 700; color: #1E293B; margin-top: 1.5rem; }
    .univ-card {
        background-color: #FFFDFB;
        padding: 14px 20px;
        border-radius: 8px;
        border-left: 5px solid #991B1B;
        border-top: 1px solid #E2E8F0;
        border-right: 1px solid #E2E8F0;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 8px;
    }
    code {
        color: #B91C1C;
        background-color: #FEF2F2;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

# Dynamic Temporal Constraint Engine (Anchored to current environment)
current_date = datetime.date.today()
CURRENT_YEAR = current_date.year
NEXT_YEAR = CURRENT_YEAR + 1
CURRENT_MONTH_STR = current_date.strftime("%B")

# Strict mode uses precision hooks; Broad mode uses loose future-anchors
STRICT_TEMPORAL = f'("{CURRENT_YEAR}" OR "{NEXT_YEAR}" OR "upcoming" OR "{CURRENT_MONTH_STR} {CURRENT_YEAR}")'
BROAD_TEMPORAL = f'("{CURRENT_YEAR}" OR "{NEXT_YEAR}" OR "upcoming")'

st.title("✊🏽 Critical Geography & Radical Humanities Engine")
st.markdown("##### Dual-Mode Portal Tracking Across National Research Intensities, Departmental Feeds, and Funding Matrices")
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
# INTEGRATED MASTER RESEARCH HUBS (Including Requested Elite Nodes)
# =====================================================================
TOP_50_HUMANITIES_GEOGRAPHY = [
    {
        "name": "Centre for the Study of Developing Societies (CSDS)", 
        "type": "Elite Radical Humanities Node", 
        "dept": '("CSDS" OR "Social and Political Theory" OR "Lokniti" OR "Digital Methods")',
        "feed_path": "https://www.csds.in/events/announcements"
    },
    {
        "name": "Indian Institute for Human Settlements (IIHS)", 
        "type": "Elite Spatial & Transition Node", 
        "dept": '("IIHS" OR "Urban ARC" OR "Geospatial Lab" OR "Spatial Analytics Unit")',
        "feed_path": "https://iihs.co.in/research/conferences/"
    },
    {
        "name": "IIIT Hyderabad (HSRC / Spatial Labs)", 
        "type": "Computational-Humanities Intersection", 
        "dept": '("Human Sciences Research Centre" OR "HSRC" OR "Lab for Spatial Informatics" OR "C2S2")',
        "feed_path": "https://hsrc.iiit.ac.in/"
    },
    {
        "name": "IIT Delhi (HSS Department)", 
        "type": "Premium Tech-Humanities Node", 
        "dept": '("Department of Humanities and Social Sciences" OR "IITD HSS" OR "Public Systems Lab")',
        "feed_path": "https://hss.iitd.ac.in/"
    },
    {
        "name": "IIT Bombay (HSS / CSRE)", 
        "type": "Premium Tech-Humanities Node", 
        "dept": '("Humanities and Social Sciences" OR "HSS" OR "CSRE" OR "Socio-Spatial Mapping")',
        "feed_path": "https://www.csre.iitb.ac.in/news.php"
    },
    {
        "name": "IIT Gandhinagar (HSS Department)", 
        "type": "Premium Tech-Humanities Node", 
        "dept": '("Humanities and Social Sciences" OR "IITGN HSS" OR "Digital Humanities Lab")',
        "feed_path": "https://hss.iitgn.ac.in/"
    },
    {
        "name": "IIT Madras (HSS Department)", 
        "type": "Premium Tech-Humanities Node", 
        "dept": '("Humanities and Social Sciences" OR "IITM HSS" OR "Urban Systems Lab")',
        "feed_path": "https://hss.iitm.ac.in/"
    },
    {
        "name": "Jawaharlal Nehru University", 
        "type": "Interdisciplinary Powerhouse", 
        "dept": '("Centre for the Study of Regional Development" OR "CSRD" OR "Centre for Social Medicine and Community Health" OR "CSMCH")',
        "feed_path": "https://www.jnu.ac.in/events"
    },
    {
        "name": "Delhi School of Economics", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography" OR "DSE")',
        "feed_path": "https://www.du.ac.in/index.php?page=notifications"
    },
    {
        "name": "Aligarh Muslim University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography" OR "AMU")',
        "feed_path": "https://www.amu.ac.in/departments/geography/notices"
    },
    {
        "name": "Banaras Hindu University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography" OR "BHU")',
        "feed_path": "https://bhu.ac.in/Site/Notification/"
    },
    {
        "name": "Jamia Millia Islamia", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography" OR "JMI")',
        "feed_path": "https://www.jmi.ac.in/bulletinboard/notices/latest"
    },
    {
        "name": "Tata Institute of Social Sciences", 
        "type": "Specialized Intersectionality Hub", 
        "dept": '("School of Rural Development" OR "Centre for Study of Social Exclusion and Inclusive Policies" OR "TISS")',
        "feed_path": "https://tiss.edu/view/6/announcements/tiss-announcements/"
    },
    {
        "name": "Panjab University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://puchd.ac.in/notices.php"
    },
    {
        "name": "University of Calcutta", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.caluniv.ac.in/news/news.html"
    },
    {
        "name": "University of Madras", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.unom.ac.in/index.php?route=administration/notices"
    },
    {
        "name": "Savitribai Phule Pune University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography" OR "Interdisciplinary Studies")',
        "feed_path": "http://www.unipune.ac.in/university_files/notification.htm"
    },
    {
        "name": "Dr. Harisingh Gour Vishwavidyalaya", 
        "type": "Regional & Rural Development Node", 
        "dept": '("School of Studies in Geography" OR "SoS in Geography" OR "Anthropology")',
        "feed_path": "http://www.dhsgsu.edu.in/index.php/en/notices"
    },
    {
        "name": "Vikram University", 
        "type": "Regional & Rural Development Node", 
        "dept": '("School of Studies in Geography" OR "Institute of Social Science")',
        "feed_path": "http://www.vikramuniv.ac.in/index.php/en/notices-circulars"
    },
    {
        "name": "Barkatullah University", 
        "type": "Regional & Rural Development Node", 
        "dept": '("Department of Geography")',
        "feed_path": "http://www.bubhopal.ac.in/1053/Circulars-and-Orders"
    },
    {
        "name": "Rani Durgavati Vishwavidyalaya", 
        "type": "Regional & Rural Development Node", 
        "dept": '("Department of Geography")',
        "feed_path": "http://www.rdunijbpin.org/1172/Notifications"
    },
    {
        "name": "Giri Institute of Development Studies", 
        "type": "Specialized Policy / Margin Tracking", 
        "dept": '("GIDS")',
        "feed_path": "http://gids.org.in/events/"
    },
    {
        "name": "Institute of Economic Growth", 
        "type": "Specialized Policy / Margin Tracking", 
        "dept": '("IEG")',
        "feed_path": "https://www.iegindia.org/events_seminars/"
    },
    {
        "name": "Centre for Development Studies", 
        "type": "Specialized Policy / Margin Tracking", 
        "dept": '("CDS")',
        "feed_path": "https://cds.edu/news-events/"
    },
    {
        "name": "Osmania University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.osmania.ac.in/news-notifications.php"
    },
    {
        "name": "University of Allahabad", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://allduniv.ac.in/p/65/notifications"
    },
    {
        "name": "Patna University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://pup.ac.in/notice.html"
    },
    {
        "name": "Gauhati University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.gauhati.ac.in/notifications"
    },
    {
        "name": "Utkal University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://utkaluniversity.ac.in/notices/"
    },
    {
        "name": "Rajasthan University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.uniraj.ac.in/index.php?toc=notice"
    },
    {
        "name": "Pt. Ravishankar Shukla University", 
        "type": "Regional & Rural Development Node", 
        "dept": '("School of Studies in Geography")',
        "feed_path": "https://www.prsu.ac.in/news"
    },
    {
        "name": "North-Eastern Hill University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography" OR "NEHU")',
        "feed_path": "https://nehu.ac.in/notifications"
    },
    {
        "name": "Ranchi University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://ranchiuniversity.ac.in/index.php?option=com_content&view=category&id=9&Itemid=128"
    },
    {
        "name": "University of Jammu", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://jammuuniversity.ac.in/notifications"
    },
    {
        "name": "CSJM University Kanpur", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://csjmu.ac.in/important-links/notices-circulars/"
    },
    {
        "name": "Kumaun University Nainital", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.kunainital.ac.in/notifications.php"
    },
    {
        "name": "Visva-Bharati University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography" OR "Vidya Bhavana")',
        "feed_path": "https://visvabharati.ac.in/AdmissionsNotices.html"
    },
    {
        "name": "Mohanlal Sukhadia University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.mlsu.ac.in/notifications.php"
    },
    {
        "name": "Gujarat University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.gujaratuniversity.ac.in/announcement"
    },
    {
        "name": "University of Mysore", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://uni-mysore.ac.in/notices-circulars"
    },
    {
        "name": "Shivaji University Kolhapur", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.unishivaji.ac.in/synopsis/Circulars"
    },
    {
        "name": "Bharathidasan University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://www.bdu.ac.in/notifications/"
    },
    {
        "name": "Kurukshetra University", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://new.kuk.ac.in/notifications-circulars/"
    },
    {
        "name": "National Institute of Rural Development", 
        "type": "Dedicated Rural Development Node", 
        "dept": '("NIRDPR")',
        "feed_path": "http://nirdpr.org.in/seminars-workshops.aspx"
    },
    {
        "name": "Institute of Rural Management Anand", 
        "type": "Dedicated Rural Development Node", 
        "dept": '("IRMA")',
        "feed_path": "https://irma.ac.in/news-and-events"
    },
    {
        "name": "Indian Institute of Remote Sensing", 
        "type": "Spatial Sciences & GIS Hub", 
        "dept": '("IIRS")',
        "feed_path": "https://www.iirs.gov.in/news-events"
    },
    {
        "name": "IIT Kanpur", 
        "type": "Spatial Sciences & GIS Hub", 
        "dept": '("Humanities and Social Sciences" OR "HSS" OR "Geoinformatics")',
        "feed_path": "https://www.iitk.ac.in/new/announcements"
    },
    {
        "name": "IIT Kharagpur", 
        "type": "Spatial Sciences & GIS Hub", 
        "dept": '("Humanities and Social Sciences" OR "HSS" OR "CORAL")',
        "feed_path": "https://www.iitkgp.ac.in/news-and-events"
    },
    {
        "name": "BIT Mesra", 
        "type": "Spatial Sciences & GIS Hub", 
        "dept": '("Department of Remote Sensing")',
        "feed_path": "https://bitmesra.ac.in/Show_Notifications?cid=1"
    },
    {
        "name": "CEPT University", 
        "type": "Spatial Sciences & GIS Hub", 
        "dept": '("Faculty of Planning" OR "Spatial Planning")',
        "feed_path": "https://cept.ac.in/news-and-events"
    },
    {
        "name": "A.N. Sinha Institute of Social Studies", 
        "type": "Specialized Policy / Margin Tracking", 
        "dept": '("ANSISS")',
        "feed_path": "http://ansiss.res.in/notifications"
    },
    {
        "name": "Centre for Policy Research", 
        "type": "Specialized Policy / Margin Tracking", 
        "dept": '("CPR")',
        "feed_path": "https://cprindia.org/events/"
    },
    {
        "name": "Madras Institute of Development Studies", 
        "type": "Specialized Policy / Margin Tracking", 
        "dept": '("MIDS")',
        "feed_path": "https://www.mids.ac.in/events/"
    },
    {
        "name": "MANAGE Hyderabad", 
        "type": "Dedicated Rural Development Node", 
        "dept": '("National Institute of Agricultural Extension Management")',
        "feed_path": "https://www.manage.gov.in/events/events.asp"
    },
    {
        "name": "MGSIRD Jabalpur", 
        "type": "Dedicated Rural Development Node", 
        "dept": '("Mahatma Gandhi State Institute of Rural Development")',
        "feed_path": "http://mgsird.mp.gov.in/training-calendar.html"
    },
    {
        "name": "Central University of Punjab", 
        "type": "Pure Geography Focus", 
        "dept": '("Department of Geography")',
        "feed_path": "https://cup.edu.in/notifications"
    }
]

# =====================================================================
# SIDEBAR CONFIGURATORS
# =====================================================================
st.sidebar.markdown("### 🗺️ Territorial Scope")
state_list = sorted(df['state'].unique().tolist())
default_state_idx = state_list.index("Madhya Pradesh") if "Madhya Pradesh" in state_list else 0
selected_state = st.sidebar.selectbox("Target Regional Node", state_list, index=default_state_idx)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📂 Structural Document Pattern")
RESOURCE_TYPES = {
    "Brochures & Notification PDFs": "(filetype:pdf OR brochure OR circular OR \"notice board\" OR \"downloads\")",
    "Conferences, Seminars & Symposia": "(national conference OR seminar OR symposium OR registration OR \"call for papers\")",
    "Methodology Workshops & Training": "(methodology workshop OR capacity building OR FDP OR \"research methodology\")"
}
chosen_resource = st.sidebar.selectbox("Target Output Format", list(RESOURCE_TYPES.keys()))

# Advanced National Funding Grid Setup
FUNDING_BODIES = '("ICSSR" OR "UGC" OR "DST" OR "CSIR" OR "ICAR" OR "Ministry of Education" OR "MoE" OR "Ministry of Rural Development" OR "MoRD")'

# =====================================================================
# DUAL-MODE COMPILER PIPELINE
# =====================================================================
resource_query = RESOURCE_TYPES[chosen_resource]

def compile_dork(institution_name, target_department_string=None, mode="strict"):
    query_elements = [f'"{institution_name}"']
    
    if target_department_string:
        query_elements.append(target_department_string)
    else:
        query_elements.append('("Geography" OR "Social Sciences" OR "Humanities" OR "Development Studies" OR "Notice Board" OR "Events")')
        
    query_elements.append(resource_query)
    
    if mode == "strict":
        # Strategy A: Hyper-targeted gold standard
        query_elements.append(FUNDING_BODIES)
        query_elements.append(STRICT_TEMPORAL)
    else:
        # Strategy B: Safety net bypasses funding grid and uses loose date anchors
        query_elements.append(BROAD_TEMPORAL)
    
    final_string = " AND ".join(query_elements)
    return f"https://www.google.com/search?q={final_string.replace(' ', '+')}"

# =====================================================================
# NEW ZONE: GLOBAL FUNDER SWEEP (CROSS-COUNTRY MATRIX SCANNER)
# =====================================================================
st.subheader("🌐 Global Funder Sweep (Cross-Country Matrix Scan)")
st.markdown("Aggressive meta-dork tracking across all 5 key Indian research domain spaces (`.ac.in`, `.res.in`, `.org.in`, `.edu`, `.gov.in`, and elite independent spaces) bypassing individual university cards to capture hidden ICSSR training grants.")

col_sweep1, col_sweep2 = st.columns(2)

with col_sweep1:
    cbp_domains = '(site:ac.in OR site:res.in OR site:org.in OR site:edu OR site:gov.in OR site:csds.in OR site:iihs.co.in)'
    cbp_dork = f'{cbp_domains} "Capacity Building" AND "ICSSR" AND ("{CURRENT_YEAR}" OR "upcoming")'
    cbp_url = f"https://www.google.com/search?q={cbp_dork.replace(' ', '+')}"
    
    st.info("🎯 **Capacity Building Programmes (CBP)**")
    st.markdown("Scans elite councils, state grids, and universities simultaneously for newly posted multi-week training tracks.")
    st.link_button("🚀 Launch Country-Wide CBP Sweep", cbp_url, use_container_width=True)

with col_sweep2:
    rmw_dork = f'{cbp_domains} "Research Methodology" AND ("Workshop" OR "FDP") AND "ICSSR"'
    rmw_url = f"https://www.google.com/search?q={rmw_dork.replace(' ', '+')}"
    
    st.info("📊 **Research Methodology Workshops (RMW)**")
    st.markdown("Sweeps the entire multi-domain network for intensive 7-to-10 day Research Methodology and Research Capacity setups.")
    st.link_button("🚀 Launch Country-Wide RMW Sweep", rmw_url, use_container_width=True)

st.markdown("---")

# =====================================================================
# DISPLAY ZONE 1: THE CRITICAL CORE NATIONAL NETWORK
# =====================================================================
st.subheader("🔥 Core Research Intensities (National Elite Nodes)")
st.markdown("Direct infrastructural pipelines matching targeted centers tracking upcoming academic frameworks and funding structures.")

for idx, item in enumerate(TOP_50_HUMANITIES_GEOGRAPHY):
    with st.container():
        st.markdown(f"""
        <div class="univ-card">
            <h4>🏫 {item['name']}</h4>
            <p style='margin-top:-5px; color:#64748B; font-size:14px;'>
                <strong>Structural Pattern:</strong> {item['type']} | <strong>Target Context Core:</strong> <code>{item['dept']}</code>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_action1, col_action2, col_action3 = st.columns([1, 1.3, 1.3])
        with col_action1:
            st.link_button(
                "🌐 Open Live Portal", 
                item['feed_path'], 
                use_container_width=True,
                key=f"feed_portal_{idx}"
            )
        with col_action2:
            st.link_button(
                "🔎 Strict Deep Dork", 
                compile_dork(item['name'], target_department_string=item['dept'], mode="strict"), 
                use_container_width=True,
                key=f"strict_dork_{idx}",
                help="Requires explicit funding bodies and precise current-month tracking strings."
            )
        with col_action3:
            st.link_button(
                "🔓 Broad Safety Scan", 
                compile_dork(item['name'], target_department_string=item['dept'], mode="broad"), 
                use_container_width=True,
                key=f"broad_dork_{idx}",
                help="Bypasses funding matrices to catch un-sponsored or localized department notices."
            )
        st.markdown("<br>", unsafe_allow_html=True)

# =====================================================================
# DISPLAY ZONE 2: TERRITORIAL HUB COMPLETE INDEX
# =====================================================================
st.subheader(f"🏛️ Territorial Registry Landscape Node: {selected_state}")
st.markdown("Comprehensive scanning coverage over registered state institutional infrastructure nodes to pick up local cross-disciplinary layouts.")

filtered_state_df = df[df['state'] == selected_state].sort_values(by='Name of the University')

if not filtered_state_df.empty:
    for idx, row in filtered_state_df.iterrows():
        univ_name = row['Name of the University']
        
        with st.container():
            st.markdown(f"**🏛️ {univ_name}**  \n📍 `Registry Address String:` {row['Address']}")
            
            col_state_btn1, col_state_btn2 = st.columns([1, 1])
            with col_state_btn1:
                st.link_button(
                    "🔎 Run Strict Scan", 
                    compile_dork(univ_name, mode="strict"), 
                    use_container_width=True, 
                    key=f"state_strict_{idx}"
                )
            with col_state_btn2:
                st.link_button(
                    "🔓 Run Broad Safety Scan", 
                    compile_dork(univ_name, mode="broad"), 
                    use_container_width=True, 
                    key=f"state_broad_{idx}"
                )
            st.markdown("---")
else:
    st.warning("No dynamic structural nodes populated for this state configuration inside the master index layer.")
