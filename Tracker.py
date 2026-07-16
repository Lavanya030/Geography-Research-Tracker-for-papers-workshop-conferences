import streamlit as st
import urllib.parse
import datetime

# Page configuration
st.set_page_config(page_title="Pro Academic Event Tracker", page_icon="🎓", layout="wide")

st.title("🎓 Pro Academic Event & Notice Board Tracker")
st.markdown("### *Advanced Global Multi-Disciplinary Discovery Engine*")
st.write("Customize your keywords, add custom universities, and batch-search academic networks globally.")
st.divider()

# Auto-calculate current tracking year (2026)
current_year = datetime.date.today().year

# =====================================================================
# 1. DYNAMIC DISCIPLINARY KEYWORDS (NOW EDITABLE)
# =====================================================================
st.sidebar.header("🛠️ 1. Edit Discipline Keywords")
st.sidebar.write("Fine-tune the search terms for your field below:")

DEFAULT_DISCIPLINE_MAP = {
    "🌍 Geography": '"geography" OR "human geography" OR "regional development" OR "spatial justice" OR "urban studies"',
    "👥 Sociology": '"sociology" OR "social research" OR "social theory" OR "demography" OR "caste" OR "class" OR "gender"',
    "💼 Management & Policy": '"management" OR "public policy" OR "development studies" OR "governance" OR "organizational studies"',
    "🏺 Anthropology": '"anthropology" OR "ethnography" OR "cultural studies" OR "fieldwork" OR "indigenous"',
    "📜 History": '"history" OR "historical geography" OR "archives" OR "historiography" OR "agrarian history"',
    "🛰️ GIS & Geoinformatics": '"GIS" OR "geoinformatics" OR "spatial analysis" OR "remote sensing" OR "spatial data science" OR "mapping"'
}

# Allow the researcher to view and live-edit the query parameters
selected_discipline = st.sidebar.selectbox("Select Discipline to Edit/Use:", list(DEFAULT_DISCIPLINE_MAP.keys()))
active_keywords = st.sidebar.text_area(
    "Active Keywords (Edit freely):", 
    value=DEFAULT_DISCIPLINE_MAP[selected_discipline],
    height=100
)

# Set custom date filters
st.sidebar.markdown("---")
st.sidebar.header("📅 2. Date Constraints")
target_year = st.sidebar.number_input("Primary Target Year:", min_value=2020, max_value=2035, value=current_year)
include_next_year = st.sidebar.checkbox("Include Next Year in search?", value=True)

# Build date filter string
if include_next_year:
    date_filter = f'("{target_year}" OR "{target_year + 1}")'
else:
    date_filter = f'"{target_year}"'

# =====================================================================
# 2. UNIVERSITY REGISTRY (WITH CUSTOM DOMAIN ADDER)
# =====================================================================
GLOBAL_REGISTRY = {
    "🇮🇳 India": [
        {"inst": "Jawaharlal Nehru University (JNU)", "domain": "jnu.ac.in"},
        {"inst": "University of Delhi (DU)", "domain": "du.ac.in"},
        {"inst": "Tata Institute of Social Sciences (TISS)", "domain": "tiss.edu"},
        {"inst": "Banaras Hindu University (BHU)", "domain": "bhu.ac.in"},
        {"inst": "Jamia Millia Islamia (JMI)", "domain": "jmi.ac.in"},
        {"inst": "Aligarh Muslim University (AMU)", "domain": "amu.ac.in"},
        {"inst": "IIT Bombay", "domain": "iitb.ac.in"},
        {"inst": "IIT Kharagpur", "domain": "iitkgp.ac.in"}
    ],
    "🇬🇧 United Kingdom": [
        {"inst": "University of Oxford", "domain": "ox.ac.uk"},
        {"inst": "University of Cambridge", "domain": "cam.ac.uk"},
        {"inst": "London School of Economics (LSE)", "domain": "lse.ac.uk"},
        {"inst": "University College London (UCL)", "domain": "ucl.ac.uk"},
        {"inst": "SOAS University of London", "domain": "soas.ac.uk"}
    ],
    "🇺🇸 United States": [
        {"inst": "Harvard University", "domain": "harvard.edu"},
        {"inst": "University of California, Berkeley", "domain": "berkeley.edu"},
        {"inst": "University of Chicago", "domain": "uchicago.edu"},
        {"inst": "Penn State University", "domain": "psu.edu"},
        {"inst": "Clark University", "domain": "clarku.edu"}
    ]
}

# --- CUSTOM UNIVERSITY ADDER ---
st.subheader("🔗 Add a Custom University Domain")
col_name, col_dom, col_btn = st.columns([3, 3, 2])

# Initialize session state for custom universities if not exists
if "custom_unis" not in st.session_state:
    st.session_state.custom_unis = []

with col_name:
    custom_name = st.text_input("University Name:", placeholder="e.g., London School of Geography", key="cust_name")
with col_dom:
    custom_domain = st.text_input("Domain (No https/www):", placeholder="e.g., geography.org", key="cust_dom")
with col_btn:
    st.write(" ") # alignment spacer
    st.write(" ") 
    if st.button("➕ Add to My Search Network", use_container_width=True):
        if custom_name and custom_domain:
            # Strip common url prefixes if user accidentally pastes them
            clean_domain = custom_domain.replace("https://", "").replace("http://", "").replace("www.", "").strip("/")
            st.session_state.custom_unis.append({"inst": custom_name, "domain": clean_domain})
            st.success(f"Added {custom_name}!")
            st.rerun()

# Combine static registry with user-added universities
combined_registry = GLOBAL_REGISTRY.copy()
if st.session_state.custom_unis:
    combined_registry["⭐ Custom Registered Universities"] = st.session_state.custom_unis

# =====================================================================
# 3. INTERACTIVE SEARCH INTERFACE
# =====================================================================
st.divider()
st.subheader("🔍 Institutional Scanning Portal")

region = st.selectbox("Select Target Network:", list(combined_registry.keys()))
active_list = combined_registry[region]

st.write(f"Showing **{len(active_list)}** universities in this network. Adjust your target discipline settings in the left sidebar.")

# Display Grid
for i in range(0, len(active_list), 2):
    row_unis = active_list[i:i+2]
    cols = st.columns(2, gap="large")
    
    for idx, uni in enumerate(row_unis):
        with cols[idx]:
            # Clean Layout Card
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; padding: 15px; border-radius: 8px; margin-bottom: 5px; background-color: #f9f9f9;">
                    <h4 style="margin: 0; color: #2e6f40;">🏫 {uni['inst']}</h4>
                    <p style="margin: 5px 0; font-size: 0.9em; color: #555;"><strong>Active Search Domain:</strong> <code>{uni['domain']}</code></p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Formulate the Google Dorks using our dynamic variables
            discipline_query = f"({active_keywords})"
            
            # PDF Search Syntax
            pdf_query = f'site:{uni["domain"]} filetype:pdf {discipline_query} AND ("seminar" OR "conference" OR "workshop" OR "call for papers" OR "colloquium") AND {date_filter}'
            encoded_pdf = urllib.parse.quote_plus(pdf_query)
            
            # Directory Search Syntax
            dir_query = f'site:{uni["domain"]}/events OR site:{uni["domain"]}/seminars OR site:{uni["domain"]}/news {discipline_query} AND {date_filter}'
            encoded_dir = urllib.parse.quote_plus(dir_query)
            
            # Buttons
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.link_button(
                    "📄 Scan PDF Circulars", 
                    f"https://www.google.com/search?q={encoded_pdf}", 
                    use_container_width=True,
                    type="primary"
                )
            with btn_col2:
                st.link_button(
                    "🗂️ Scan Web Bulletins", 
                    f"https://www.google.com/search?q={encoded_dir}", 
                    use_container_width=True
                )
            st.write("") # spacing

# =====================================================================
# 4. SYSTEM STATUS / TROUBLESHOOTING
# =====================================================================
st.divider()
st.subheader("🛠️ Active Dork Template (Current Selection)")
st.write("Copy this exact template to manually search a website if needed:")
sample_dork = f'site:example.edu filetype:pdf ({active_keywords}) AND ("seminar" OR "conference" OR "workshop" OR "call for papers") AND {date_filter}'
st.code(sample_dork, language="sql")
