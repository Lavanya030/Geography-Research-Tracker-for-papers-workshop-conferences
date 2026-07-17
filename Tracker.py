import streamlit as st
import pandas as pd
import datetime
import os

# =====================================================================
# 1. CORE ENGINE & UI CONFIG
# =====================================================================
st.set_page_config(page_title="Geography Engine", layout="wide")

# CSS Styling - MAINTAINED
st.markdown("""
    <style>
    .univ-card { background-color: #FAFAFA; padding: 15px; border-radius: 8px; border-left: 5px solid #7F1D1D; margin-bottom: 10px; border: 1px solid #E2E8F0; }
    h1 { color: #7F1D1D; font-weight: 800; }
    h3 { color: #1E293B; font-weight: 700; }
    .funder-header { margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

current_date = datetime.date.today()
CURRENT_YEAR = current_date.year

def load_base_registry():
    # Ensure this looks for your actual CSV
    file_name = "Welcome to UGC, New Delhi, India.csv"
    if os.path.exists(file_name):
        return pd.read_csv(file_name), True
    return pd.DataFrame(columns=['Name of the University', 'state', 'Address']), False

def get_dork_url(institution_name, resource_type, mode="strict"):
    base = f'"{institution_name}"'
    patterns = {
        "Conferences, Seminars & Symposia": "(conference OR seminar OR symposium OR \"call for papers\")",
        "Methodology Workshops & Training": "(\"methodology workshop\" OR \"capacity building\" OR FDP)",
        "Brochures & Notification PDFs": "(filetype:pdf OR brochure OR circular OR \"notice board\")"
    }
    pattern = patterns.get(resource_type, "")
    if mode == "strict":
        query = f"{base} AND {pattern} AND (\"upcoming\" OR \"{CURRENT_YEAR}\")"
    else:
        query = f"{base} AND {pattern}"
    return f"https://www.google.com/search?q={query.replace(' ', '+')}"

# =====================================================================
# 2. ELITE RESEARCH HUBS (Full List Restored)
# =====================================================================
TOP_50_NODES = [
    {"name": "Jawaharlal Nehru University (CSRD)", "path": "https://www.jnu.ac.in"},
    {"name": "Delhi School of Economics", "path": "https://www.du.ac.in"},
    {"name": "Aligarh Muslim University", "path": "https://www.amu.ac.in"},
    {"name": "Centre for the Study of Developing Societies (CSDS)", "path": "https://www.csds.in"},
    {"name": "Indian Institute for Human Settlements (IIHS)", "path": "https://iihs.co.in"},
    {"name": "Tata Institute of Social Sciences", "path": "https://tiss.edu"},
    {"name": "IIT Delhi (HSS Department)", "path": "https://hss.iitd.ac.in"},
    {"name": "IIT Bombay (HSS)", "path": "https://www.iitb.ac.in"},
    {"name": "University of Hyderabad", "path": "https://uohyd.ac.in"},
    {"name": "Panjab University", "path": "https://puchd.ac.in"},
]

# =====================================================================
# 3. SIDEBAR CONTROLS
# =====================================================================
df, success = load_base_registry()
st.sidebar.markdown("### 🗺️ Territorial Scope")
state_list = sorted(df['state'].unique().tolist()) if not df.empty else ["No Data"]
selected_state = st.sidebar.selectbox("Select State", state_list)

st.sidebar.markdown("### 📂 Structural Document Pattern")
chosen_resource = st.sidebar.selectbox("Document Type", [
    "Conferences, Seminars & Symposia", 
    "Methodology Workshops & Training", 
    "Brochures & Notification PDFs"
])

# =====================================================================
# 4. RENDERING ENGINE
# =====================================================================
st.title("✊🏽 Geography Engine")

# --- Elite Section ---
st.subheader("🔥 Core Research Intensities (National Elite Nodes)")
for item in TOP_50_NODES:
    with st.container():
        st.markdown(f"**🏫 {item['name']}**")
        c1, c2, c3 = st.columns(3)
        with c1: st.link_button("🌐 Portal", item['path'])
        with c2: st.link_button("🔎 Strict", get_dork_url(item['name'], chosen_resource, "strict"))
        with c3: st.link_button("🔓 Broad", get_dork_url(item['name'], chosen_resource, "broad"))

# --- Reactive State Registry ---
st.markdown("---")
filtered_df = df[df['state'] == selected_state] if not df.empty else pd.DataFrame()
st.subheader(f"🏛️ Territorial Registry: {selected_state}")

for _, row in filtered_df.iterrows():
    univ = row['Name of the University']
    with st.container():
        st.markdown(f'<div class="univ-card"><strong>{univ}</strong></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.link_button("🔎 Strict", get_dork_url(univ, chosen_resource, "strict"))
        with c2: st.link_button("🔓 Broad", get_dork_url(univ, chosen_resource, "broad"))

# --- Global Funder Sweep (Restored to exact spec) ---
st.markdown("---")
st.subheader("🌐 Global Funder Sweep (Cross-Country Matrix Scan)")
st.markdown(f"**Current Structural Filter Selection:** `{chosen_resource}`")

col_sweep1, col_sweep2 = st.columns(2)
cbp_domains = '(site:ac.in OR site:res.in OR site:org.in OR site:edu OR site:gov.in)'

with col_sweep1:
    cbp_dork = f'{cbp_domains} "Capacity Building" AND "ICSSR" AND {CURRENT_YEAR}'
    st.info("🎯 **Capacity Building Programmes (CBP)**")
    st.link_button("🚀 Launch Country-Wide CBP Sweep", f"https://www.google.com/search?q={cbp_dork.replace(' ', '+')}", use_container_width=True)

with col_sweep2:
    rmw_dork = f'{cbp_domains} "Research Methodology" AND ("Workshop" OR "FDP") AND "ICSSR" AND {CURRENT_YEAR}'
    st.info("📊 **Research Methodology Workshops (RMW)**")
    st.link_button("🚀 Launch Country-Wide RMW Sweep", f"https://www.google.com/search?q={rmw_dork.replace(' ', '+')}", use_container_width=True)
