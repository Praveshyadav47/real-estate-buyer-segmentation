import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Real Estate Buyer Segmentation",
    page_icon="🏠",
    layout="wide"
)

# Load data
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

buyer_data = pd.read_csv(
    DATA_DIR / "app_buyer_data.csv"
)

cluster_profile = pd.read_csv(
    DATA_DIR / "cluster_profile.csv"
)

# Title
st.title("🏠 Real Estate Buyer Segmentation")

st.subheader(
    "Machine Learning-Based Buyer Segmentation and Investment Profiling"
)

st.write(
    """
    This application uses K-Means clustering to segment real-estate
    buyers based on demographic, investment, property ownership,
    satisfaction, and behavioral characteristics.
    """
)

# Dataset overview
st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Buyers", len(buyer_data))

with col2:
    st.metric("Number of Clusters", buyer_data["cluster"].nunique())

with col3:
    st.metric("Features", len(buyer_data.columns) - 1)

# Cluster distribution
st.header("Buyer Cluster Distribution")

cluster_counts = (
    buyer_data["cluster"]
    .value_counts()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    cluster_counts.index.astype(str),
    cluster_counts.values
)

ax.set_xlabel("Cluster")
ax.set_ylabel("Number of Buyers")
ax.set_title("Number of Buyers by Cluster")

st.pyplot(fig)

# Cluster profile
st.header("Cluster Profile")

profile = cluster_profile.copy()

if "Unnamed: 0" in profile.columns:
    profile = profile.drop(columns=["Unnamed: 0"])

st.dataframe(
    profile,
    use_container_width=True
)

# Average investment
st.header("Average Investment by Cluster")

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    profile["cluster"].astype(str),
    profile["avg_investment"]
)

ax.set_xlabel("Cluster")
ax.set_ylabel("Average Investment (USD)")
ax.set_title("Average Investment by Buyer Cluster")

st.pyplot(fig)

# Average properties
st.header("Average Properties Owned")

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    profile["cluster"].astype(str),
    profile["avg_properties"]
)

ax.set_xlabel("Cluster")
ax.set_ylabel("Average Number of Properties")
ax.set_title("Average Properties Owned by Cluster")

st.pyplot(fig)

# Business insights
st.header("Business Insights")

st.markdown(
    """
### Cluster 0 – Large, Lower-Investment Segment

- Represents approximately 54.15% of buyers.
- Average investment is approximately $1.05M.
- Buyers own approximately 3.54 properties on average.
- Average satisfaction score is 2.96.

### Cluster 1 – Higher-Property-Value Segment

- Represents approximately 43.35% of buyers.
- Average investment is approximately $1.46M.
- Average property value is approximately $409K.
- Average property size is approximately 1,344.

### Cluster 2 – Small, High-Investment Segment

- Represents approximately 2.50% of buyers.
- Average investment is approximately $2.42M.
- Buyers own approximately 7.32 properties on average.
- Average satisfaction score is 3.52.
- Website acquisition represents approximately 70% of this cluster.

### Recommendations

- Develop differentiated strategies for each buyer segment.
- Use digital channels to engage high-investment buyers.
- Promote higher-value properties to Cluster 1.
- Analyze satisfaction drivers in Cluster 0.
- Monitor Cluster 2 separately because of its higher average investment and property ownership.
"""
)

# Footer
st.markdown("---")

st.caption(
    "Real Estate Buyer Segmentation | K-Means Clustering | Data Analyst Internship Project"
)