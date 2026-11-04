from components.sidebar import render_sidebar
import streamlit as st
import pandas as pd

from api.client import get_data




# ==================================================
# Population
# ==================================================

dashboard = get_data("/dashboard")



render_sidebar()

st.header("👥 Population Health")

pop = dashboard["population"]

summary = pop["patient_summary"]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Patients", f"{summary['total_patients']:,}")
c2.metric("Average Age", f"{summary['average_age']:.2f}")
c3.metric("Male Patients", summary["male_patients"])
c4.metric("Female Patients", summary["female_patients"])

st.subheader("Population KPIs")

kpi = pop["population_kpis"]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Avg Visits", round(kpi["avg_visits"], 2))
c2.metric("Avg Cost", f"${kpi['avg_cost']:,.2f}")
c3.metric("Total Cost", f"${kpi['total_cost']:,.0f}")
c4.metric("High Risk Patients", kpi["high_risk_patients"])

st.subheader("Age Distribution")

age_df = pd.DataFrame(pop["age_distribution"])

st.bar_chart(
age_df.set_index("age_group")
)

st.subheader("Gender Distribution")

gender_df = pd.DataFrame(
pop["gender_distribution"]
)

st.dataframe(
gender_df,
width='stretch'
)

st.divider()

# ==================================================
# Clinical
# ==================================================

st.header("🩺 Clinical Analytics")

clinical = dashboard["clinical"]

summary = clinical["clinical_summary"]

c1, c2, c3 = st.columns(3)

c1.metric(
"Total Patients",
summary["total_patients"]
)

c2.metric(
"Chronic Patients",
summary["chronic_patients"]
)

c3.metric(
"Abnormal Lab Patients",
summary["abnormal_lab_patients"]
)

st.subheader("Top Diagnoses")

st.dataframe(
pd.DataFrame(
clinical["top_diagnoses"]
),
width='stretch'
)

labs = clinical["abnormal_labs"]

st.info(
f"""
Total Lab Results: {labs['total_lab_results']:,}

Abnormal Results: {labs['abnormal_lab_results']:,}

Abnormal %: {labs['abnormal_lab_percentage']}%
"""
)

st.divider()

# ==================================================
# Risk
# ==================================================

st.header("⚠️ Risk Analytics")

risk = dashboard["risk"]

summary = risk["risk_summary"]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
"Average Risk Score",
round(summary["average_risk_score"], 2)
)

c2.metric(
"Max Risk Score",
summary["maximum_risk_score"]
)

c3.metric(
"Min Risk Score",
summary["minimum_risk_score"]
)

c4.metric(
"High Risk Patients",
risk["high_risk_patients"]
)

risk_df = pd.DataFrame(
risk["risk_distribution"]
)

st.bar_chart(
risk_df.set_index("risk_category")
)

st.divider()

# ==================================================
# Cost
# ==================================================

st.header("💰 Cost Analytics")

cost = dashboard["cost"]

summary = cost["cost_summary"]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
"Total Cost",
f"${summary['total_cost']:,.0f}"
)

c2.metric(
"Average Cost",
f"${summary['average_cost']:,.0f}"
)

c3.metric(
"Max Cost",
f"${summary['maximum_cost']:,.0f}"
)

c4.metric(
"High Cost Patients",
cost["high_cost_patients"]
)

st.subheader("Payer Analysis")

st.dataframe(
pd.DataFrame(
cost["payer_analysis"]
),
width='stretch'
)

st.divider()

# ==================================================
# Utilization
# ==================================================

st.header("🏥 Utilization Analytics")

util = dashboard["utilization"]

summary = util["utilization_summary"]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
"Total Visits",
summary["total_visits"]
)

c2.metric(
"Avg Visits / Patient",
round(
summary["average_visits_per_patient"],
2
)
)

c3.metric(
"Average LOS",
round(summary["average_los"], 2)
)

c4.metric(
"Readmission %",
f"{summary['readmission_rate_pct']}%"
)

st.divider()

# ==================================================
# Segmentation
# ==================================================

st.header("🎯 Patient Segmentation")

seg = dashboard["segmentation"]

st.subheader("Segment Distribution")

seg_df = pd.DataFrame(
seg["segment_distribution"]
)

st.bar_chart(
seg_df.set_index("segment")
)

st.subheader("Segment Summary")

st.dataframe(
pd.DataFrame(
seg["segment_summary"]
),
width='stretch'
)

c1, c2 = st.columns(2)

c1.success(
f"""
High Value Segment

Segment: {seg['high_value_segment']['segment']}

Avg Cost: ${seg['high_value_segment']['average_cost']:,.0f}
"""
)

c2.warning(
f"""
High Risk Segment

Segment: {seg['high_risk_segment']['segment']}

Average Risk: {seg['high_risk_segment']['average_risk']}
"""
)

