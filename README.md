🛍️ Customer Shopping Behavior Analysis

Python | PostgreSQL | Power BI

An end-to-end data analytics project analyzing 3,900 customer purchase transactions to uncover insights into revenue patterns, customer loyalty, product performance, and subscription behavior.

📌 Project Overview

This project explores transactional shopping data to answer key business questions and generate strategic recommendations. The analysis pipeline includes:

Data cleaning & feature engineering in Python

Business analysis in PostgreSQL (SQL)

Interactive dashboard creation in Power BI

The goal is to transform raw transactional data into actionable insights for decision-making.

📊 Dataset Summary

Rows: 3,900

Columns: 18

Missing Values: 37 (Review Rating column – imputed using category median)

Key Features:

Customer Demographics (Age, Gender, Location, Subscription Status)

Purchase Details (Item, Category, Amount, Season, Size, Color)

Behavior Metrics (Discount Applied, Frequency, Previous Purchases, Review Rating, Shipping Type)

🧹 Data Preparation (Python)

Performed in analysis.py:

Data loading using pandas

Missing value imputation (median by category)

Column standardization (snake_case)

Feature engineering:

age_group

purchase_frequency_days

Removed redundant columns

Exported cleaned dataset

Uploaded data to PostgreSQL

🗄 SQL Business Analysis

Key business questions answered:

Revenue by gender

High-spending discount users

Top 5 products by average rating

Shipping type comparison

Subscribers vs non-subscribers revenue

Discount-dependent products

Customer segmentation (New / Returning / Loyal)

Top 3 products per category (CTE + Window Functions)

Repeat buyers vs subscription correlation

Revenue by age group

📈 Power BI Dashboard

The interactive dashboard includes:

KPIs (Total Customers, Avg Purchase, Avg Rating)

Sales by Category

Revenue by Age Group

Subscription Distribution

Customer Segmentation

Shipping Preferences

🔎 Key Insights

Male customers generate 2x more revenue than female customers

79.9% of customers are loyal buyers

Non-subscribers generate higher total revenue

High-discount products drive sales but impact margins

Young adults contribute highest revenue

🎯 Business Recommendations

Promote subscription benefits

Strengthen loyalty programs

Optimize discount strategy

Target high-revenue age groups

Focus on express-shipping users

🛠 Tech Stack

Python (Pandas, NumPy)

PostgreSQL

SQL (CTEs, Window Functions)

Power BI

Psycopg2 / SQLAlchemy

📂 Project Structure
├── customer_shopping_behavior.csv
├── analysis.py
├── customer_shopping_cleaned.csv
├── SQL_queries.sql
├── customer_behavior_analysis.pbix
├── Customer-Shopping-Behavior-Analysis.pptx
└── README.md
🚀 How to Run
1️⃣ Python Analysis
python analysis.py
2️⃣ Connect to PostgreSQL

Ensure PostgreSQL is running and database:

customer_behavior_analysis
3️⃣ Open Dashboard

Open customer_behavior_analysis.pbix in Power BI Desktop.

💡 Skills Demonstrated

Data Cleaning & Feature Engineering

SQL Business Analytics

Window Functions & CTEs

Dashboard Storytelling

Business Insight Extraction

Database Integration
