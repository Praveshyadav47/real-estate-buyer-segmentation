\# 🏠 Real Estate Buyer Segmentation



\## Machine Learning-Based Buyer Segmentation and Investment Profiling



This project uses machine learning and data analysis techniques to segment real-estate buyers based on investment behavior, property ownership, satisfaction, and demographic characteristics.



\## 📊 Project Overview



The project analyzes 2,000 real-estate buyers and applies K-Means clustering to identify distinct buyer segments.



\### Key Technologies



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- Matplotlib

\- Seaborn

\- Streamlit

\- Jupyter Notebook



\## 🤖 Machine Learning



K-Means clustering was used for buyer segmentation.



The number of clusters was evaluated using:



\- Elbow Method

\- Silhouette Score



The final model uses \*\*3 buyer clusters\*\*.



\## 📈 Key Buyer Segments



\### Cluster 0 — Lower-Investment Segment



\- Represents approximately 54.15% of buyers

\- Average investment: approximately $1.05M

\- Average properties owned: 3.54

\- Average satisfaction score: 2.96



\### Cluster 1 — Higher-Property-Value Segment



\- Represents approximately 43.35% of buyers

\- Average investment: approximately $1.46M

\- Average property value: approximately $409K

\- Average property size: approximately 1,344



\### Cluster 2 — Small, High-Investment Segment



\- Represents approximately 2.50% of buyers

\- Average investment: approximately $2.42M

\- Average properties owned: 7.32

\- Average satisfaction score: 3.52



\## 📊 Dashboard



A Streamlit dashboard was developed to visualize:



\- Buyer cluster distribution

\- Cluster-level investment patterns

\- Property ownership

\- Buyer segment profiles

\- Business insights



\## 📁 Project Structure



```text

real-estate-buyer-segmentation/

│

├── app/

│   └── app.py

│

├── data/

│   ├── app\_buyer\_data.csv

│   └── cluster\_profile.csv

│

├── notebooks/

│   └── real\_estate\_buyer\_segmentation.ipynb

│

├── outputs/

│

├── requirements.txt

├── .gitignore

└── README.md

