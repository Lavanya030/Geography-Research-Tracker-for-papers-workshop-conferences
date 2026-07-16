import streamlit as st
import urllib.parse
import datetime

# Page configuration
st.set_page_config(page_title="Geography Event Tracker", page_icon="🌍", layout="wide")

st.title("🌍 Geography Academic Event Tracker Dashboard")
st.markdown("### *Zero-Noise Institutional Notice Board Scanner*")
st.write("This tool targets the exact subdirectories and PDF circular structures where universities publish their active seminars and calls.")
st.divider()

# Get today's automatic rolling year to prevent prehistoric results
current_year = datetime.date.today().year # e.g., 2026

# =====================================================================
# 1. PARAMETERS
# =====================================================================
st.sidebar.header("🎯 Focus Keywords")

# Free text input - keep keywords simple for maximum search results
custom_focus = st.sidebar.text_input(
    "1. Define Topic/Discipline:",
    value="geography OR rural OR spatial",
    help="Keep terms simple (e.g. 'geography', 'rural development', 'spatial analysis')"
)

# Clean, unified keywords
discipline_keywords = f"({custom_focus})"

st.sidebar.markdown("---")
st.sidebar.info(f"📅 Showing only results containing year references **{current_year}** or **{current_year + 1}**")

# =====================================================================
# 2. UNIVERSITY NETWORKS
# =====================================================================
REGIONAL_NETWORKS = {
    "🇮🇳 India Academic Network (.ac.in)": [
        {"inst": "Jawaharlal Nehru University", "domain": "jnu.ac.in", "dept": "CSRD / School of Social Sciences"},
        {"inst": "Delhi University", "domain": "du.ac.in", "dept": "Department of Geography"},
        {"inst": "Banaras Hindu University", "domain": "bhu.ac.in", "dept": "Department of Geography"},
        {"inst": "Jamia Millia Islamia", "domain": "jmi.ac.in", "dept": "Department of Geography"},
        {"inst": "Aligarh Muslim University", "domain": "amu.ac.in", "dept": "Department of Geography"},
        {"inst": "IIT Bombay", "domain": "iitb.ac.in", "dept": "Humanities & Social Sciences (HSS)"},
        {"inst": "IIT Kharagpur", "domain": "iitkgp.ac.in", "dept": "Humanities & Social Sciences"}
    ],
    "🇬🇧 United Kingdom Network (.ac.uk)": [
        {"inst": "University of Oxford", "domain": "ox.ac.uk", "dept": "School of Geography and the Environment"},
        {"inst": "University of Cambridge", "domain": "cam.ac.uk", "dept": "Department of Geography"},
        {"inst": "University College London", "domain": "ucl.ac.uk", "dept": "Department of Geography"},
        {"inst": "University of Edinburgh", "domain": "ed.ac.uk", "dept": "School of GeoSciences"},
        {"inst": "University of Liverpool", "domain": "liverpool.ac.uk", "dept": "Department of Geography & Planning"}
    ],
    "🇺🇸 United States Network (.edu)": [
        {"inst": "Clark University", "domain": "clarku.edu", "dept": "Graduate School of Geography"},
        {"inst": "Penn State University", "domain": "psu.edu", "dept": "Department of Geography"},
        {"inst": "UC Berkeley", "domain": "berkeley.edu", "dept": "Department of Geography"},
        {"inst": "University of Washington", "domain": "washington.edu", "dept": "Department of Geography"}
    ]
}

selected_network = st.selectbox("📂 Select Regional Network to View:", list(REGIONAL_NETWORKS.keys()))
active_list = REGIONAL_NETWORKS[selected_network]

# =====================================================================
# 3. CARD GRID LAYOUT
# =====================================================================
st.subheader(f"Dashboard: {selected_network}")
st.write("Academic departments rarely publish clean HTML event pages. Use these targeted buttons to scan their raw PDFs or their direct system directories:")

for i in range(0, len(active_list), 2):
    row_unis = active_list[i:i+2]
    cols = st.columns(2, gap="medium")
    
    for idx, uni in enumerate(row_unis):
        with cols[idx]:
            st.markdown(
                f"""
                <div style="border: 1px solid #e0e0e0; padding: 15px; border-radius: 8px; margin-bottom: 5px; background-color: #fcfcfc;">
                    <h4 style="margin: 0; color: #1f77b4;">🏫 {uni['inst']}</h4>
                    <p style="margin: 4px 0; font-size: 0.9em; color: #666;"><strong>Domain:</strong> <code>{uni['domain']}</code> | <strong>Unit:</strong> {uni['dept']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # --- BUTTON 1: SCAN RAW SEMINAR & CONFERENCE PDFs ---
            # This directly captures the newly uploaded PDF circular sheets (highly effective for JNU/IITs)
            pdf_query = f'site:{uni["domain"]} filetype:pdf {discipline_keywords} AND ("seminar" OR "conference" OR "workshop" OR "call for papers") AND ("{current_year}" OR "{current_year + 1}")'
            encoded_pdf = urllib.parse.quote_plus(pdf_query)
            
            # --- BUTTON 2: LIVE DIRECTORY SCANNER ---
            # This directly scans structural event directories of the university
            dir_query = f'site:{uni["domain"]}/events OR site:{uni["domain"]}/seminars OR site:{uni["domain"]}/news {discipline_keywords} AND ("{current_year}" OR "{current_year + 1}")'
            encoded_dir = urllib.parse.quote_plus(dir_query)
            
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.link_button(
                    "📄 Scan Call PDFs", 
                    f"https://www.google.com/search?q={encoded_pdf}", 
                    use_container_width=True,
                    type="primary"
                )
            with btn_col2:
                st.link_button(
                    "🗂️ Scan Event Directories", 
                    f"https://www.google.com/search?q={encoded_dir}", 
                    use_container_width=True
                )
            st.write("") # Spacer

st.divider()
st.caption("Global Geography Discovery Engine • Direct Filetype & Directory Mapping.")
