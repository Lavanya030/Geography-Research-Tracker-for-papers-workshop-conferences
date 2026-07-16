import streamlit as st
import urllib.parse
import datetime

# Page configuration
st.set_page_config(page_title="Geography Event Tracker", page_icon="🌍", layout="wide")

st.title("🌍 Geography Academic Event Tracker Dashboard")
st.markdown("### *One-Click Portal for Individual University Monitoring*")
st.write("Below is your tracking network. Simply find the university you want to audit and click its search button to pull its live, upcoming events.")
st.divider()

# =====================================================================
# 1. AUTOMATIC ROLLING DATE SYSTEM
# =====================================================================
# This automatically calculates future months so search results are current
today = datetime.date.today()
current_month_idx = today.month  # e.g., 7 for July
current_year = today.year        # e.g., 2026

months_names = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Generate future month strings for the current year
remaining_months = months_names[current_month_idx - 1:]
future_month_strings = [f'"{month} {current_year}"' for month in remaining_months]

# Add next year as a catch-all for far-off deadlines
next_year_string = f'"{current_year + 1}"'
all_future_dates = future_month_strings + [next_year_string]

# This ensures we only find pages with text pointing to today or the future
date_text_filter = "(" + " OR ".join(all_future_dates) + ")"

# =====================================================================
# 2. SELECT REGION
# =====================================================================
REGIONAL_NETWORKS = {
    "🇮🇳 India Academic Network (.ac.in)": [
        {"inst": "Jawaharlal Nehru University", "domain": "jnu.ac.in", "dept": "Center for the Study of Regional Development (CSRD)"},
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

# = "Global Geography Search" Config
st.sidebar.header("🎯 Target Discipline")
discipline = st.sidebar.selectbox(
    "Focus Area:",
    ["Socio-Spatial, Rural & Regional Development", "GIScience & Spatial Analysis"]
)

# Set keywords based on discipline
if "Socio-Spatial" in discipline:
    discipline_keywords = '("geography" OR "rural" OR "regional development" OR "socio-spatial")'
else:
    discipline_keywords = '("GIS" OR "spatial data science" OR "geoinformatics" OR "remote sensing")'

st.sidebar.markdown("---")
st.sidebar.success("📅 **Live Auto-Filter Active**")
st.sidebar.write(f"Searching events scheduled from **{months_names[current_month_idx-1]} {current_year}** onwards.")

# =====================================================================
# 3. DISPLAY THE INTERACTIVE CARD GRID
# =====================================================================
st.subheader(f"Dashboard: {selected_network}")
st.write("Click any university's action buttons below to open a direct, clean Google search for that institution's active schedules.")

# Display universities in columns
for i in range(0, len(active_list), 2):
    # Process two universities per row for a clean grid layout
    row_unis = active_list[i:i+2]
    cols = st.columns(2, gap="medium")
    
    for idx, uni in enumerate(row_unis):
        with cols[idx]:
            # Create a visual card structure using markdown
            st.markdown(
                f"""
                <div style="border: 1px solid #e6e6e6; padding: 15px; border-radius: 8px; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #ff4b4b;">🏫 {uni['inst']}</h4>
                    <p style="margin: 5px 0; font-size: 0.9em; color: #555;"><strong>Domain:</strong> <code>{uni['domain']}</code></p>
                    <p style="margin: 5px 0; font-size: 0.9em; color: #555;"><strong>Primary Unit:</strong> {uni['dept']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Formulate the highly focused search query for THIS SPECIFIC university
            dept_query = f'site:{uni["domain"]} {discipline_keywords} AND ("workshop" OR "conference" OR "seminar" OR "symposium" OR "call for papers") AND {date_text_filter}'
            encoded_dept = urllib.parse.quote_plus(dept_query)
            
            # Formulate research group/lab search query for THIS SPECIFIC university
            lab_query = f'site:{uni["domain"]} {discipline_keywords} AND ("research center" OR "working group" OR "lab") AND ("news" OR "events" OR "activities") AND {date_text_filter}'
            encoded_lab = urllib.parse.quote_plus(lab_query)
            
            # Place action buttons side-by-side inside the card column
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.link_button(
                    "📅 Seminars & CFPs", 
                    f"https://www.google.com/search?q={encoded_dept}", 
                    use_container_width=True
                )
            with btn_col2:
                st.link_button(
                    "🔬 Research Labs/Centers", 
                    f"https://www.google.com/search?q={encoded_lab}", 
                    use_container_width=True
                )
            st.write("") # Spacer

st.divider()
st.caption("Global Geography Discovery Engine • Optimized for individual site verification.")
