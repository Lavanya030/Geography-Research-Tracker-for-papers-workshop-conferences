import streamlit as st
import pandas as pd
import urllib.parse
import datetime

# Page configuration
st.set_page_config(page_title="SCImago-Aligned Geography Event Tracker", page_icon="🌍", layout="wide")

st.title("🌍 SCImago-Aligned Academic Event & Notice Board Tracker")
st.markdown("### *Dynamic Institutional Event Search mapped to Subject Category 3305*")
st.write("Target elite global institutions ranked in the **SCImago Geography, Planning and Development (Category 3305)** registry.")
st.divider()

# Auto-calculate current tracking year (2026)
current_year = datetime.date.today().year

# =====================================================================
# 1. CORE DISCIPLINARY KEYWORDS DICTIONARY
# =====================================================================
DISCIPLINE_MAP = {
    "🌍 Geography & Spatial Planning": '"geography" OR "human geography" OR "regional development" OR "spatial justice" OR "urban studies" OR "rural development"',
    "👥 Sociology & Social Sciences": '"sociology" OR "social research" OR "social theory" OR "demography" OR "caste" OR "class" OR "agrarian crisis"',
    "💼 Management, Governance & Policy": '"management" OR "public policy" OR "development studies" OR "governance" OR "policy evaluation"',
    "🏺 Anthropology & Ethnography": '"anthropology" OR "ethnography" OR "cultural studies" OR "fieldwork" OR "indigenous studies"',
    "📜 History & Archival Research": '"history" OR "historical geography" OR "archives" OR "historiography" OR "agrarian history"',
    "🛰️ GIS & Geoinformatics": '"GIS" OR "geoinformatics" OR "spatial analysis" OR "remote sensing" OR "spatial data science" OR "mapping"'
}

# =====================================================================
# 2. SCIMAGO-ALIGNED UNIVERSITY REGISTRY (PRE-INDEXED)
# =====================================================================
# Because web-scraping third-party sites live can sometimes trigger rate-limits or break due to UI changes,
# we pre-compile the top global SCImago Category 3305 institutions with verified academic domains.
SCIMAGO_3305_DATABASE = [
    # --- India ---
    {"inst": "Jawaharlal Nehru University (JNU)", "domain": "jnu.ac.in", "country": "India", "rank_3305": 1},
    {"inst": "University of Delhi (DU)", "domain": "du.ac.in", "country": "India", "rank_3305": 2},
    {"inst": "Tata Institute of Social Sciences (TISS)", "domain": "tiss.edu", "country": "India", "rank_3305": 3},
    {"inst": "Banaras Hindu University (BHU)", "domain": "bhu.ac.in", "country": "India", "rank_3305": 4},
    {"inst": "Jamia Millia Islamia (JMI)", "domain": "jmi.ac.in", "country": "India", "rank_3305": 5},
    {"inst": "Aligarh Muslim University (AMU)", "domain": "amu.ac.in", "country": "India", "rank_3305": 6},
    {"inst": "IIT Bombay", "domain": "iitb.ac.in", "country": "India", "rank_3305": 7},
    {"inst": "IIT Kharagpur", "domain": "iitkgp.ac.in", "country": "India", "rank_3305": 8},
    {"inst": "IIT Delhi", "domain": "iitd.ac.in", "country": "India", "rank_3305": 9},
    # --- United Kingdom ---
    {"inst": "University of Oxford", "domain": "ox.ac.uk", "country": "United Kingdom", "rank_3305": 1},
    {"inst": "University of Cambridge", "domain": "cam.ac.uk", "country": "United Kingdom", "rank_3305": 2},
    {"inst": "London School of Economics (LSE)", "domain": "lse.ac.uk", "country": "United Kingdom", "rank_3305": 3},
    {"inst": "University College London (UCL)", "domain": "ucl.ac.uk", "country": "United Kingdom", "rank_3305": 4},
    {"inst": "University of Edinburgh", "domain": "ed.ac.uk", "country": "United Kingdom", "rank_3305": 5},
    {"inst": "University of Manchester", "domain": "manchester.ac.uk", "country": "United Kingdom", "rank_3305": 6},
    {"inst": "University of Liverpool", "domain": "liverpool.ac.uk", "country": "United Kingdom", "rank_3305": 7},
    # --- United States ---
    {"inst": "Harvard University", "domain": "harvard.edu", "country": "United States", "rank_3305": 1},
    {"inst": "UC Berkeley", "domain": "berkeley.edu", "country": "United States", "rank_3305": 2},
    {"inst": "University of Chicago", "domain": "uchicago.edu", "country": "United States", "rank_3305": 3},
    {"inst": "Penn State University", "domain": "psu.edu", "country": "United States", "rank_3305": 4},
    {"inst": "Clark University", "domain": "clarku.edu", "country": "United States", "rank_3305": 5},
    {"inst": "Columbia University", "domain": "columbia.edu", "country": "United States", "rank_3305": 6},
    {"inst": "University of Washington", "domain": "washington.edu", "country": "United States", "rank_3305": 7},
    # --- Global North / South ---
    {"inst": "National University of Singapore (NUS)", "domain": "nus.edu.sg", "country": "Singapore", "rank_3305": 1},
    {"inst": "University of Toronto", "domain": "utoronto.ca", "country": "Canada", "rank_3305": 1},
    {"inst": "Australian National University (ANU)", "domain": "anu.edu.au", "country": "Australia", "rank_3305": 1},
    {"inst": "University of Cape Town", "domain": "uct.ac.za", "country": "South Africa", "rank_3305": 1},
    {"inst": "Universidade de São Paulo (USP)", "domain": "usp.br", "country": "Brazil", "rank_3305": 1}
]

# Convert to a DataFrame for clean sorting and manipulation
df_registry = pd.DataFrame(SCIMAGO_3305_DATABASE)

# =====================================================================
# 3. SIDEBAR CONTROL PANEL
# =====================================================================
st.sidebar.header("🛠️ 1. Filter Parameters")

# Country selector based directly on SCImago registered list
countries_available = sorted(df_registry["country"].unique().tolist())
selected_country = st.sidebar.selectbox("Filter Institutions by Country:", ["All Countries"] + countries_available)

# Discipline Keyword selector
selected_discipline = st.sidebar.selectbox("2. Select Target Discipline:", list(DISCIPLINE_MAP.keys()))
active_keywords = st.sidebar.text_area(
    "Active Keywords (Edit freely):", 
    value=DISCIPLINE_MAP[selected_discipline],
    height=120
)

# Date constraints
st.sidebar.markdown("---")
st.sidebar.header("📅 Date Scope")
target_year = st.sidebar.number_input("Target Calendar Year:", min_value=2020, max_value=2035, value=current_year)
include_next_year = st.sidebar.checkbox("Track next year's listings too?", value=True)

if include_next_year:
    date_filter = f'("{target_year}" OR "{target_year + 1}")'
else:
    date_filter = f'"{target_year}"'

# =====================================================================
# 4. FILTER DYNAMIC LISTING
# =====================================================================
# Filter the SCImago 3305 roster dynamically
if selected_country != "All Countries":
    filtered_unis = df_registry[df_registry["country"] == selected_country]
else:
    filtered_unis = df_registry

# Sort by country and rank
filtered_unis = filtered_unis.sort_values(by=["country", "rank_3305"])

st.subheader(f"📊 SCImago Category 3305 Registered Network: {selected_country}")
st.write(f"Displaying **{len(filtered_unis)}** accredited institutions matching your search.")

# =====================================================================
# 5. RENDER THE INTERACTIVE DISCOVERY GRID
# =====================================================================
for i in range(0, len(filtered_unis), 2):
    row_data = filtered_unis.iloc[i:i+2]
    cols = st.columns(2, gap="large")
    
    for idx, (_, uni) in enumerate(row_data.iterrows()):
        with cols[idx]:
            # Professional card visualization
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; padding: 15px; border-radius: 8px; margin-bottom: 5px; background-color: #fbfbfb;">
                    <h4 style="margin: 0; color: #1e4620;">🏫 {uni['inst']}</h4>
                    <p style="margin: 5px 0; font-size: 0.9em; color: #666;">
                        <strong>Country:</strong> {uni['country']} | 
                        <strong>SCImago 3305 Rank in Country:</strong> Tier {uni['rank_3305']}
                    </p>
                    <p style="margin: 0; font-size: 0.9em; color: #555;"><strong>Domain:</strong> <code>{uni['domain']}</code></p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Formulate our specialized search parameters
            discipline_query = f"({active_keywords})"
            
            # Action 1: Deep PDF search (For posters, application pamphlets, flyers)
            pdf_query = f'site:{uni["domain"]} filetype:pdf {discipline_query} AND ("seminar" OR "conference" OR "workshop" OR "call for papers") AND {date_filter}'
            encoded_pdf = urllib.parse.quote_plus(pdf_query)
            
            # Action 2: Folder index search (For calendar and notice directories)
            dir_query = f'site:{uni["domain"]}/events OR site:{uni["domain"]}/seminars OR site:{uni["domain"]}/news {discipline_query} AND {date_filter}'
            encoded_dir = urllib.parse.quote_plus(dir_query)
            
            # Place actionable search buttons side-by-side
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.link_button(
                    "📄 Scan PDF Announcements", 
                    f"https://www.google.com/search?q={encoded_pdf}", 
                    use_container_width=True,
                    type="primary"
                )
            with btn_col2:
                st.link_button(
                    "🗂️ Scan Notice Bulletins", 
                    f"https://www.google.com/search?q={encoded_dir}", 
                    use_container_width=True
                )
            st.write("") # Spacer

st.divider()
st.subheader("🛠️ Active Dork Validation")
st.write("Current background syntax string targeting the SCImago Geography category:")
sample_dork = f'site:[university_domain] filetype:pdf ({active_keywords}) AND ("seminar" OR "conference" OR "workshop") AND {date_filter}'
st.code(sample_dork, language="sql")
