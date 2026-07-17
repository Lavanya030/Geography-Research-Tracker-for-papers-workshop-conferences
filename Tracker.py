import streamlit as st
import pandas as pd
import datetime
import os

# Set up clean, professional page configurations
st.set_page_config(
    page_title="Academic Funding Discovery Engine", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Clean CSS Injection for Academic UI Polish
st.markdown("""
    <style>
    .main .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    h1 { font-weight: 800; color: #1E3A8A; letter-spacing: -0.5px; }
    .stAlert { border-radius: 8px; border: none; }
    .card-box {
        background-color: #F8FAFC;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .badge-high {
        background-color: #DCFCE7; color: #15803D;
        padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 13px;
    }
    .badge-mod {
        background-color: #FEF9C3; color: #854D0E;
        padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 13px;
    }
    .compliance-check {
        color: #0F766E; font-weight: 500; font-size: 14px; margin-top: 8px;
    }
    .compliance-warn {
        color: #B91C1C; font-weight: 500; font-size: 14px; margin-top: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# TEMPORAL ANCHOR ENGINE (AUTOMATED CURRENT DATE TRACKING)
# =====================================================================
CURRENT_YEAR = datetime.datetime.now().year
ACADEMIC_SESSION_QUERY = f"({CURRENT_YEAR} OR {CURRENT_YEAR}-{str(CURRENT_YEAR+1)[2:]})"

# Top Banner Brand
st.title("🎓 Academic Infrastructure & Funding Discovery Engine")
st.markdown("##### System Environment: Automated Rolling Academic Session Engine Locked to Current Context")
st.markdown("---")

# =====================================================================
# DATA INITIALIZATION & 12(B) COMPLIANCE ANALYSIS
# =====================================================================
@st.cache_data
def load_and_score_infrastructure():
    file_name = "Welcome to UGC, New Delhi, India.csv"
    if os.path.exists(file_name):
        try:
            data = pd.read_csv(file_name)
            data.columns = [c.strip() for c in data.columns]
            
            data['Name of the University'] = data['Name of the University'].astype(str).str.strip()
            data['state'] = data['state'].astype(str).str.strip()
            data['Type'] = data['Type'].astype(str).str.strip()
            data['Status'] = data['Status'].astype(str).str.strip()
            data['Zip'] = data['Zip'].fillna('').astype(str).str.strip()
            
            # SCORING ALGORITHM BASED ON STATUTORY GRANT CAPACITY
            def evaluate_funding_potential(row):
                score = 20  
                u_type = row['Type'].lower()
                status = row['Status'].lower()
                
                if 'central' in u_type: score += 40
                elif 'state' in u_type: score += 25
                if '12(b)' in status: score += 30
                if 'category-i' in status: score += 10
                
                return min(score, 100)

            data['AI_Priority_Score'] = data.apply(evaluate_funding_potential, axis=1)
            return data, True
        except Exception as e:
            return None, f"Registry Parsing Error: {str(e)}"
    return None, False

df, success = load_and_score_infrastructure()

if success is not True:
    st.error("🚨 CRITICAL SYSTEM DISRUPTION: Master database file 'Welcome to UGC, New Delhi, India.csv' not found.")
    st.info("Ensure the exact file is uploaded inside the identical root repository folder.")
    st.stop()

# =====================================================================
# CONTROL STRATEGY INTERFACE (SIDEBAR)
# =====================================================================
st.sidebar.markdown("### 🗺️ Territorial Scope")
state_list = sorted(df['state'].unique().tolist())
default_state_idx = state_list.index("Madhya Pradesh") if "Madhya Pradesh" in state_list else 0
selected_state = st.sidebar.selectbox("Target Regional Node", state_list, index=default_state_idx)

funding_compliance = st.sidebar.radio(
    "Grants Compliance Filter",
    ["Show All Registered Hubs", "Strict 12(B) Grant Eligible Only"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💎 Allocation Pipelines")
FUNDING_PIPELINES = {
    "ICSSR Structural Funding (Capacity Building & Seminars)": "ICSSR capacity building seminar conference",
    "DST-FIST / Spatial Science Schemes (GIS & Remote Sensing)": "DST FIST GIS geospatial workshop",
    "UGC Disciplinary Budget Line Items (National Conferences)": "UGC sponsored seminar call for papers",
    "MoRD / NABARD Allocations (Rural Development & Education Policy)": "Ministry of Rural Development policy workshop seminar"
}
chosen_pipeline = st.sidebar.selectbox("Grant Pipeline Engine", list(FUNDING_PIPELINES.keys()))
core_subject = st.sidebar.selectbox("Domain Isolation Parameter", ["Geography", "Rural Development", "Education Policy", "Social Sciences"])

# =====================================================================
# DATA FILTERING & WEIGHTING RUNS
# =====================================================================
processed_df = df[df['state'] == selected_state].copy()

if funding_compliance == "Strict 12(B) Grant Eligible Only":
    processed_df = processed_df[processed_df['Status'].str.contains('12\(B\)', case=False, na=False)]

processed_df = processed_df.sort_values(by='AI_Priority_Score', ascending=False)

# =====================================================================
# APP LAYOUT GENERATION
# =====================================================================
# Real-time analytics block metrics card layout
metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric(label="Total Tracked Hubs in Region", value=len(processed_df))
with metric_col2:
    total_eligible = len(processed_df[processed_df['Status'].str.contains('12\(B\)', case=False, na=False)])
    st.metric(label="12(B) Grant-Eligible Assets", value=total_eligible)
with metric_col3:
    st.metric(label="Temporal Session Filter", value=f"{CURRENT_YEAR} Window")

st.markdown("---")

if not processed_df.empty:
    # AUTOMATED MACRO CLUSTER ACCELERATOR CARD
    st.markdown("### ⚡ Dynamic Macro Cluster Aggregator")
    st.markdown("Consolidates the top grant-eligible institutional lines inside this specific state into a clean query chunk to run single-click regional environment checks.")
    
    cluster_targets = processed_df.head(4)
    target_names_query = " OR ".join([f'"{name}"' for name in cluster_targets['Name of the University']])
    pipeline_query = FUNDING_PIPELINES[chosen_pipeline]
    
    macro_query = f"({target_names_query}) AND ({pipeline_query}) AND ({core_subject}) {ACADEMIC_SESSION_QUERY}"
    macro_url = f"https://www.google.com/search?q={macro_query.replace(' ', '+')}"
    
    st.link_button(f"🚀 Batch Scan High-Probability {selected_state} Hubs", macro_url, type="primary", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📋 Verified Regional Institutional Index")
    
    # INDIVIDUAL CARD RENDER MATRIX
    for idx, row in processed_df.iterrows():
        # Custom clean bounding box card layout block
        st.markdown(f"""
            <div class="card-box">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <span style="font-size: 20px; font-weight: 700; color: #1E293B;">🏫 {row['Name of the University']}</span>
                        <div style="margin-top: 6px; color: #64748B; font-size: 14px;">
                            📍 <b>Location:</b> {row['Address']} | 🗺️ <b>PIN:</b> {row['Zip']}
                        </div>
                        <div style="margin-top: 4px; color: #475569; font-size: 14px;">
                            🏷️ <b>Tier Group:</b> {row['Type']} | 📊 <b>UGC Status:</b> Section {row['Status']}
                        </div>
                    </div>
                    <div>
                        <span class="{ 'badge-high' if int(row['AI_Priority_Score']) >= 80 else 'badge-mod' }">
                            Weight: {int(row['AI_Priority_Score'])}%
                        </span>
                    </div>
                </div>
                <div class="{ 'compliance-check' if '12(b)' in row['Status'].lower() else 'compliance-warn' }">
                    { '✅ Verified Funding Compliance: Holds explicit legal 12(B) validation clearances for Central/ICSSR grant streams.' if '12(b)' in row['Status'].lower() else '⚠️ Regulatory Constraint Alert: Lacks active 12(B) registry markers. Focus checks on localized corporate allocations.' }
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Trigger Action Buttons aligned to the bounding layout card boxes
        zip_modifier = f"AND \"{row['Zip']}\"" if row['Zip'] else ""
        ind_query = f'"{row["Name of the University"]}" {zip_modifier} AND ({pipeline_query}) AND ({core_subject}) {ACADEMIC_SESSION_QUERY}'
        ind_url = f"https://www.google.com/search?q={ind_query.replace(' ', '+')}"
        
        col_space, col_btn = st.columns([5, 1])
        with col_btn:
            st.link_button("🎯 Target Active CFPs", ind_url, use_container_width=True)
        st.markdown("<br>", unsafe_transform=True)
else:
    st.warning("No institutions located matching the chosen structural constraints.")
