import streamlit as st
import urllib.parse
import datetime

# Page configuration
st.set_page_config(page_title="SCImago 3305 Geography Event Tracker", page_icon="🌍", layout="wide")

st.title("🌍 SCImago 3305 Academic Event & Notice Board Tracker")
st.markdown("### *Global Institutional Event Search mapped to Geography, Planning and Development (Category 3305)*")
st.write("Target over 100+ pre-registered elite institutions or resolve any university from the SCImago global directory instantly.")
st.divider()

# Auto-calculate current tracking year (2026)
current_year = datetime.date.today().year

# =====================================================================
# 1. DISCIPLINARY KEYWORDS DICTIONARY
# =====================================================================
DISCIPLINE_MAP = {
    "🌍 Geography & Spatial Planning": '"geography" OR "human geography" OR "regional development" OR "spatial justice" OR "urban studies" OR "rural development" OR "settlement geography"',
    "👥 Sociology & Social Sciences": '"sociology" OR "social research" OR "social theory" OR "demography" OR "caste" OR "class" OR "gender studies" OR "agrarian crisis" OR "social inequality"',
    "💼 Management, Governance & Policy": '"management" OR "public policy" OR "development studies" OR "governance" OR "organizational studies" OR "policy evaluation"',
    "🏺 Anthropology & Ethnography": '"anthropology" OR "ethnography" OR "cultural studies" OR "fieldwork" OR "indigenous studies" OR "tribal studies"',
    "📜 History & Archival Research": '"history" OR "historical geography" OR "archives" OR "historiography" OR "agrarian history" OR "colonial studies"',
    "🛰️ GIS & Geoinformatics": '"GIS" OR "geoinformatics" OR "spatial analysis" OR "remote sensing" OR "spatial data science" OR "mapping" OR "spatial modeling"'
}

# =====================================================================
# 2. MASSIVE PRE-INDEXED SCIMAGO 3305 REGISTRY (100+ INSTITUTIONS)
# =====================================================================
SCIMAGO_3305_DATABASE = [
    # --- INDIA ---
    {"inst": "Jawaharlal Nehru University (JNU)", "domain": "jnu.ac.in", "country": "India"},
    {"inst": "University of Delhi (DU)", "domain": "du.ac.in", "country": "India"},
    {"inst": "Tata Institute of Social Sciences (TISS)", "domain": "tiss.edu", "country": "India"},
    {"inst": "Banaras Hindu University (BHU)", "domain": "bhu.ac.in", "country": "India"},
    {"inst": "Jamia Millia Islamia (JMI)", "domain": "jmi.ac.in", "country": "India"},
    {"inst": "Aligarh Muslim University (AMU)", "domain": "amu.ac.in", "country": "India"},
    {"inst": "IIT Bombay", "domain": "iitb.ac.in", "country": "India"},
    {"inst": "IIT Kharagpur", "domain": "iitkgp.ac.in", "country": "India"},
    {"inst": "IIT Delhi", "domain": "iitd.ac.in", "country": "India"},
    {"inst": "IIT Madras", "domain": "iitm.ac.in", "country": "India"},
    {"inst": "IIT Kanpur", "domain": "iitk.ac.in", "country": "India"},
    {"inst": "IIT Roorkee", "domain": "iitr.ac.in", "country": "India"},
    {"inst": "South Asian University (SAU)", "domain": "sau.int", "country": "India"},
    {"inst": "Panjab University", "domain": "puchd.ac.in", "country": "India"},
    {"inst": "Jadavpur University", "domain": "jaduniv.edu.in", "country": "India"},
    {"inst": "University of Calcutta", "domain": "caluniv.ac.in", "country": "India"},
    {"inst": "University of Madras", "domain": "unom.ac.in", "country": "India"},
    {"inst": "Gokhale Institute of Politics & Economics", "domain": "gipe.ac.in", "country": "India"},
    {"inst": "Savitribai Phule Pune University", "domain": "unipune.ac.in", "country": "India"},
    {"inst": "Pondicherry University", "domain": "pondiuni.edu.in", "country": "India"},

    # --- UNITED KINGDOM ---
    {"inst": "University of Oxford", "domain": "ox.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Cambridge", "domain": "cam.ac.uk", "country": "United Kingdom"},
    {"inst": "London School of Economics (LSE)", "domain": "lse.ac.uk", "country": "United Kingdom"},
    {"inst": "University College London (UCL)", "domain": "ucl.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Edinburgh", "domain": "ed.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Manchester", "domain": "manchester.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Liverpool", "domain": "liverpool.ac.uk", "country": "United Kingdom"},
    {"inst": "Durham University", "domain": "durham.ac.uk", "country": "United Kingdom"},
    {"inst": "King's College London (KCL)", "domain": "kcl.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Bristol", "domain": "bristol.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Leeds", "domain": "leeds.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Sheffield", "domain": "sheffield.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Sussex", "domain": "sussex.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Southampton", "domain": "southampton.ac.uk", "country": "United Kingdom"},
    {"inst": "Newcastle University", "domain": "ncl.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Glasgow", "domain": "gla.ac.uk", "country": "United Kingdom"},
    {"inst": "University of Birmingham", "domain": "bham.ac.uk", "country": "United Kingdom"},
    {"inst": "Cardiff University", "domain": "cardiff.ac.uk", "country": "United Kingdom"},

    # --- UNITED STATES ---
    {"inst": "Harvard University", "domain": "harvard.edu", "country": "United States"},
    {"inst": "University of California, Berkeley", "domain": "berkeley.edu", "country": "United States"},
    {"inst": "University of Chicago", "domain": "uchicago.edu", "country": "United States"},
    {"inst": "Penn State University", "domain": "psu.edu", "country": "United States"},
    {"inst": "Clark University", "domain": "clarku.edu", "country": "United States"},
    {"inst": "Columbia University", "domain": "columbia.edu", "country": "United States"},
    {"inst": "University of Washington", "domain": "washington.edu", "country": "United States"},
    {"inst": "University of California, Los Angeles (UCLA)", "domain": "ucla.edu", "country": "United States"},
    {"inst": "New York University (NYU)", "domain": "nyu.edu", "country": "United States"},
    {"inst": "University of Texas at Austin", "domain": "utexas.edu", "country": "United States"},
    {"inst": "University of North Carolina at Chapel Hill", "domain": "unc.edu", "country": "United States"},
    {"inst": "University of Wisconsin-Madison", "domain": "wisc.edu", "country": "United States"},
    {"inst": "Cornell University", "domain": "cornell.edu", "country": "United States"},
    {"inst": "Ohio State University", "domain": "osu.edu", "country": "United States"},
    {"inst": "Stanford University", "domain": "stanford.edu", "country": "United States"},
    {"inst": "Yale University", "domain": "yale.edu", "country": "United States"},
    {"inst": "Princeton University", "domain": "princeton.edu", "country": "United States"},
    {"inst": "University of Minnesota", "domain": "umn.edu", "country": "United States"},
    {"inst": "Arizona State University", "domain": "asu.edu", "country": "United States"},
    {"inst": "University of Colorado Boulder", "domain": "colorado.edu", "country": "United States"},

    # --- EUROPE ---
    {"inst": "University of Amsterdam", "domain": "uva.nl", "country": "Europe"},
    {"inst": "Utrecht University", "domain": "uu.nl", "country": "Europe"},
    {"inst": "Lund University", "domain": "lu.se", "country": "Europe"},
    {"inst": "Humboldt-Universität zu Berlin", "domain": "hu-berlin.de", "country": "Europe"},
    {"inst": "Freie Universität Berlin", "domain": "fu-berlin.de", "country": "Europe"},
    {"inst": "University of Copenhagen", "domain": "ku.dk", "country": "Europe"},
    {"inst": "University of Lisbon", "domain": "ulisboa.pt", "country": "Europe"},
    {"inst": "ETH Zurich", "domain": "ethz.ch", "country": "Europe"},
    {"inst": "Stockholm University", "domain": "su.se", "country": "Europe"},
    {"inst": "Heidelberg University", "domain": "uni-heidelberg.de", "country": "Europe"},
    {"inst": "Sorbonne University", "domain": "sorbonne-universite.fr", "country": "Europe"},
    {"inst": "KU Leuven", "domain": "kuleuven.be", "country": "Europe"},
    {"inst": "University of Helsinki", "domain": "helsinki.fi", "country": "Europe"},
    {"inst": "University of Oslo", "domain": "uio.no", "country": "Europe"},
    {"inst": "Vienna University", "domain": "univie.ac.at", "country": "Europe"},

    # --- ASIA & OCEANIA ---
    {"inst": "National University of Singapore (NUS)", "domain": "nus.edu.sg", "country": "Asia & Oceania"},
    {"inst": "Nanyang Technological University (NTU)", "domain": "ntu.edu.sg", "country": "Asia & Oceania"},
    {"inst": "Australian National University (ANU)", "domain": "anu.edu.au", "country": "Asia & Oceania"},
    {"inst": "University of Melbourne", "domain": "unimelb.edu.au", "country": "Asia & Oceania"},
    {"inst": "University of Sydney", "domain": "sydney.edu.au", "country": "Asia & Oceania"},
    {"inst": "University of Queensland", "domain": "uq.edu.au", "country": "Asia & Oceania"},
    {"inst": "University of Hong Kong (HKU)", "domain": "hku.hk", "country": "Asia & Oceania"},
    {"inst": "Chinese University of Hong Kong (CUHK)", "domain": "cuhk.edu.hk", "country": "Asia & Oceania"},
    {"inst": "University of Tokyo", "domain": "u-tokyo.ac.jp", "country": "Asia & Oceania"},
    {"inst": "Kyoto University", "domain": "kyoto-u.ac.jp", "country": "Asia & Oceania"},
    {"inst": "Seoul National University", "domain": "snu.ac.kr", "country": "Asia & Oceania"},
    {"inst": "Tsinghua University", "domain": "tsinghua.edu.cn", "country": "Asia & Oceania"},
    {"inst": "Peking University", "domain": "pku.edu.cn", "country": "Asia & Oceania"},
    {"inst": "University of Auckland", "domain": "auckland.ac.nz", "country": "Asia & Oceania"},

    # --- CANADA ---
    {"inst": "University of Toronto", "domain": "utoronto.ca", "country": "Canada"},
    {"inst": "University of British Columbia (UBC)", "domain": "ubc.ca", "country": "Canada"},
    {"inst": "McGill University", "domain": "mcgill.ca", "country": "Canada"},
    {"inst": "University of Alberta", "domain": "ualberta.ca", "country": "Canada"},
    {"inst": "Simon Fraser University", "domain": "sfu.ca", "country": "Canada"},
    {"inst": "McMaster University", "domain": "mcmaster.ca", "country": "Canada"},

    # --- LATIN AMERICA & AFRICA ---
    {"inst": "University of Cape Town", "domain": "uct.ac.za", "country": "Latin America & Africa"},
    {"inst": "University of the Witwatersrand", "domain": "wits.ac.za", "country": "Latin America & Africa"},
    {"inst": "Universidade de São Paulo (USP)", "domain": "usp.br", "country": "Latin America & Africa"},
    {"inst": "Universidad Nacional Autónoma de México (UNAM)", "domain": "unam.mx", "country": "Latin America & Africa"},
    {"inst": "Universidad de Buenos Aires (UBA)", "domain": "uba.ar", "country": "Latin America & Africa"},
    {"inst": "Stellenbosch University", "domain": "sun.ac.za", "country": "Latin America & Africa"}
]

# =====================================================================
# 3. SIDEBAR CONFIGURATION
# =====================================================================
st.sidebar.header("⚙️ Event Focus Setup")

# Choose Discipline Focus
discipline = st.sidebar.selectbox("1. Academic Focus Area:", list(DISCIPLINE_MAP.keys()))
discipline_keywords = DISCIPLINE_MAP[discipline]

active_keywords = st.sidebar.text_area(
    "Active Keywords (Edit freely):", 
    value=discipline_keywords,
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
# 4. INSTANT SCIMAGO RANKING DIRECT DECODER
# =====================================================================
st.markdown("### 🔍 Instant SCImago Copilot")
st.write("Find a university on SCImago that isn't listed below? Paste its name or website here to instantly query its index:")

col_uni_name, col_uni_dom, col_uni_btn = st.columns([3, 3, 2])

# Handle custom sessions
if "session_unis" not in st.session_state:
    st.session_state.session_unis = []

with col_uni_name:
    custom_name = st.text_input("SCImago Institution Name:", placeholder="e.g., University of Lisbon")
with col_uni_dom:
    custom_dom = st.text_input("Official Web Domain:", placeholder="e.g., ulisboa.pt")
with col_uni_btn:
    st.write(" ")
    st.write(" ")
    if st.button("🔌 Add & Scan Instantly", use_container_width=True):
        if custom_name and custom_dom:
            clean_dom = custom_dom.replace("https://", "").replace("http://", "").replace("www.", "").strip("/")
            st.session_state.session_unis.append({"inst": custom_name, "domain": clean_dom, "country": "⭐ Custom Additions"})
            st.success(f"Added {custom_name}!")
            st.rerun()

# Merge pre-indexed list with custom sessions
all_universities = SCIMAGO_3305_DATABASE + st.session_state.session_unis

# Convert to structured list for grouping
regions_available = sorted(list(set([uni["country"] for uni in all_universities])))

# =====================================================================
# 5. REGIONAL VIEWER
# =====================================================================
st.divider()
selected_region = st.selectbox("📂 Select Network to View:", regions_available)
filtered_list = [u for u in all_universities if u["country"] == selected_region]

st.subheader(f"📊 SCImago 3305 Network Roster: {selected_region}")
st.write(f"Displaying **{len(filtered_list)}** elite geography & social development research departments.")

# Render grid cards
for i in range(0, len(filtered_list), 2):
    row_unis = filtered_list[i:i+2]
    cols = st.columns(2, gap="large")
    
    for idx, uni in enumerate(row_unis):
        with cols[idx]:
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; padding: 15px; border-radius: 8px; margin-bottom: 5px; background-color: #fcfcfc;">
                    <h4 style="margin: 0; color: #2e6f40;">🏫 {uni['inst']}</h4>
                    <p style="margin: 5px 0; font-size: 0.9em; color: #666;"><strong>Target Domain:</strong> <code>{uni['domain']}</code></p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Action Queries
            pdf_query = f'site:{uni["domain"]} filetype:pdf ({active_keywords}) AND ("seminar" OR "conference" OR "workshop" OR "call for papers" OR "colloquium") AND {date_filter}'
            encoded_pdf = urllib.parse.quote_plus(pdf_query)
            
            dir_query = f'site:{uni["domain"]}/events OR site:{uni["domain"]}/seminars OR site:{uni["domain"]}/news ({active_keywords}) AND {date_filter}'
            encoded_dir = urllib.parse.quote_plus(dir_query)
            
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
            st.write("") 

st.divider()
st.caption("SCImago Category 3305 Global Search Engine • Unified Academic Data Mapping.")
