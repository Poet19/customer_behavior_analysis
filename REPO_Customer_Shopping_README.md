# 🛒 Customer Shopping Behavior Analysis

**Tools:** Python (Pandas, NumPy) · PostgreSQL · Power BI  
**Dataset:** 3,900+ customer transactions · 18 behavioral attributes

---

## 📌 Project Overview

This end-to-end analytics project analyzes customer shopping patterns to uncover revenue drivers, high-value segments, and purchasing trends — the kind of insights a retail or e-commerce business would use to make product and marketing decisions.

---

## 🎯 Business Questions Answered

- Which customer segments generate the most revenue?
- What products are top performers vs. underperformers?
- Are there seasonal or behavioral patterns in purchases?
- How does customer demographics affect spending?

---

## 🗂️ Project Structure

```
customer-shopping-behavior/
│
├── data/
│   └── shopping_data.csv          # Raw dataset
│
├── notebooks/
│   └── 01_EDA.ipynb               # Exploratory Data Analysis
│   └── 02_feature_engineering.ipynb
│
├── sql/
│   └── revenue_analysis.sql       # Revenue distribution queries
│   └── product_performance.sql    # Product-level analysis
│   └── customer_segments.sql      # Customer segmentation queries
│
├── dashboard/
│   └── shopping_dashboard.pbix    # Power BI dashboard file
│   └── dashboard_screenshot.png   # Preview image
│
└── README.md
```

---

## 🔍 Key Steps

### 1. Data Cleaning & EDA (Python)
- Handled missing values, outliers, and data type mismatches
- Explored distributions of age, gender, spending, and product categories
- Engineered features: purchase frequency, avg basket size, customer tier

### 2. SQL Analysis (PostgreSQL)
- Wrote 20+ queries covering:
  - Revenue by category, region, and customer segment
  - Top 10 products by sales volume and margin
  - Monthly/seasonal trend analysis
  - Customer RFM (Recency, Frequency, Monetary) segmentation

### 3. Power BI Dashboard
- 6 interactive visualizations:
  - Revenue breakdown by category and region
  - Customer demographic heatmap
  - Spending behavior by age group
  - Top products ranking
  - Monthly sales trend line
  - Customer segment distribution

---

## 📊 Key Findings

> *(Update with your actual findings before uploading)*

- Segment X accounted for ~Y% of total revenue despite being Z% of customers
- Category A consistently outperformed others across all months
- Customers aged 25–34 showed the highest average basket size

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/Poet19/customer-shopping-behavior.git
cd customer-shopping-behavior

# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# Launch notebooks
jupyter notebook notebooks/01_EDA.ipynb
```

For SQL queries, connect to a PostgreSQL instance and run files in `/sql/` in order.

---

## 📸 Dashboard Preview

*(Add a screenshot of your Power BI dashboard here)*

---

## 📬 Contact

**Gunjan Bagga** · [LinkedIn](https://linkedin.com/in/gunjan-543903230) · [gunjanbagga1819@gmail.com](mailto:gunjanbagga1819@gmail.com)
