"""
Customer Shopping Behavior Data Analysis
======================================
This script performs comprehensive data analysis on customer shopping behavior data.
It includes data cleaning, feature engineering, and exploratory data analysis (EDA)
that are commonly asked in data analysis interviews.

Purpose:
--------
This analysis aims to understand customer purchasing patterns, identify trends,
and extract meaningful insights from shopping behavior data. The script covers
end-to-end data processing workflows including data loading, cleaning, transformation,
and detailed analysis suitable for business intelligence and decision-making.

Author: Data Analysis Team
Date: 2024
Version: 1.0
"""

# Import necessary libraries for data manipulation and numerical operations
# pandas: Primary library for data manipulation and analysis (data frames ke saath kaam karta hai)
# numpy: Library for numerical computing and mathematical operations (math functions ke liye)
# Inhe import karna zaroori hai kyunki ye data analysis ke liye basic libraries hain
import pandas as pd
import numpy as np

# =============================================================================
# SECTION 1: DATA LOADING
# =============================================================================
# This section handles loading the raw customer shopping behavior data from CSV file
# The data contains various attributes about customers and their shopping patterns

# Read the CSV file 'customer_shopping_behavior.csv' and store it in DataFrame variable 'df'
# CSV (Comma Separated Values) is a common format for storing tabular data
# pd.read_csv() automatically parses the CSV file into a pandas DataFrame
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types
df = pd.read_csv('customer_shopping_behavior.csv')

# Print a formatted header to clearly mark the beginning of Data Overview section
# "=" * 60 creates a line of 60 equal signs for visual separation
print("=" * 60)
print("1. DATA OVERVIEW")
print("=" * 60)

# Display the first 5 rows of the DataFrame
# This gives us an immediate view of what the data looks like - the column names,
# data types, and sample values. It's always the first step in any data analysis
# to understand the structure and format of the data we're working with.
# head() - Ye function data ke pehle 5 rows dikhata hai, taaki hume pata chal sake
# ki data kaisa dikhta hai. Yeh data ki preview ke liye use hota hai.
print("\n--- First 5 Rows ---")
# head() by default returns the first 5 rows, giving a quick preview of the dataset
print(df.head())

# Display comprehensive information about the DataFrame
# This includes: column names, data types, non-null counts, and memory usage
# Understanding data types is crucial - it tells us whether columns are numeric,
# categorical, or text, which guides our analysis approach
# info() - Ye function poore DataFrame ki summary deta hai:
# - Kitne rows aur columns hain
# - Har column ka naam aur data type (string, number, etc.)
# - Har column mein kitne non-null values hain
# - Kitna memory use ho raha hai
# Data type samajhna zaroori hai kyunki isse humein pata chalega ki konsa column
# number hai, konsa text hai, ya konsa category hai
print("\n--- DataFrame Info ---")
# info() provides a concise summary of the DataFrame including:
# - Number of rows and columns
# - Column names and their data types
# - Number of non-null values in each column
# - Memory usage of the DataFrame
print(df.info())

# Display statistical summary of numerical columns
# This includes: count, mean, std, min, 25%, 50%, 75%, max
# These statistics help us understand the distribution, central tendency,
# and spread of numerical data. Very useful for identifying outliers and
# understanding the overall scale of values.
# describe() - Ye function numerical columns ki statistics deta hai:
# - count: Kitne values hain
# - mean: Average (sabhi values ka jodke divide karna)
# - std: Standard deviation (data kitna spread hai)
# - min: Sabse chhota value
# - 25%, 50%, 75%: Quartiles (data ke parts)
# - max: Sabse bada value
# Ye humein batata hai ki data ka pattern kaisa hai, kya koi outliers hain
print("\n--- Statistical Summary (Numerical) ---")
# describe() returns count, mean, std, min, quartiles, and max for numeric columns
print(df.describe())

# Include categorical columns in summary as well
# For categorical data, this shows: count, unique, top (most frequent), and freq
# This helps understand the cardinality of categorical variables and identify
# the most common categories in each column
# include='all' - Ye parameter batata hai ki numerical aur dono types ki columns
# ki statistics dikhayo. Categorical data ke liye:
# - count: Kitne values hain
# - unique: Kitne alag-alag values hain
# - top: Sabse zyada wala value (most frequent)
# - freq: Most frequent value kitni baar aya
print("\n--- Statistical Summary (All Columns) ---")
# include='all' includes both numerical and categorical columns in the summary
print(df.describe(include='all'))

# =============================================================================
# SECTION 2: MISSING VALUE ANALYSIS AND HANDLING
# =============================================================================
# Missing values are a common problem in real-world datasets. They can occur due to
# various reasons: data entry errors, sensor failures, survey non-responses, etc.
# This section identifies missing values and implements appropriate handling strategies.

print("\n" + "=" * 60)
print("2. MISSING VALUE ANALYSIS")
print("=" * 60)

# Check for missing values in each column
# isnull() returns a DataFrame of boolean values (True for missing, False for present)
# sum() then counts the True values for each column
# This tells us exactly how many missing values exist in each column
# isnull() - Ye har cell check karta hai ki woh empty (null) hai ya nahi
# Agar cell khali hai to True return karta hai, nahi to False
# sum() - True values ko count karta hai, isse humein pata chalega
# ki kitne cells khali hain
missing_values = df.isnull().sum()
print("\n--- Missing Values per Column ---")
# Filter to show only columns with missing values (where count > 0)
print(missing_values[missing_values > 0])

# Calculate the percentage of missing values for each column
# This is important because a small percentage might be handled differently than a large one
# Generally, if more than 5-10% values are missing, we need to be careful about imputation
# as it might significantly affect the analysis results
# len(df) - DataFrame ki total rows count karta hai
# (missing / total) * 100 - Percentage calculate karta hai
# Agar 5-10% se zyada values missing hain, toh imputation karna risky ho sakta hai
missing_pct = (df.isnull().sum() / len(df)) * 100
print("\n--- Missing Value Percentage ---")
# Show percentage only for columns with missing values
print(missing_pct[missing_pct > 0])

# Analysis shows: Review Rating has 37 missing values (~0.95% of data)
# This is a relatively small percentage, so imputation is a reasonable approach

# IMPUTATION STRATEGY EXPLANATION:
# We use the MEDIAN of review rating for each product category to fill missing values
# Why median instead of mean? 
# - Median is less sensitive to outliers (extreme values don't affect it much)
# - In customer reviews, there can be biased ratings at extremes
# - Using category-specific median preserves the relationship between category and rating
# This is a common best practice in data analysis when dealing with skewed distributions

print("\n--- Handling Missing Values in 'Review Rating' ---")
# Show how many values were missing before imputation
print(f"Missing values before: {df['Review Rating'].isnull().sum()}")

# Apply groupby with transform to fill missing values with category-specific median
# groupby('Category') groups the data by category column (har category alag group banata hai)
# transform() - Har group par function apply karta hai aur wapis DataFrame return karta hai
# lambda x: x.fillna(x.median()) - Har group mein missing values ko us group ke median se fill karta hai
# fillna() - Missing values ko fill karta hai, yahan median se
# median - Beech wala value, outliers se affect nahi hota
# groupby() - Isse hum data ko categories mein baante hain, taaki har category ke liye
# alag se calculation kar sakein
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)

# Verify that all missing values have been filled
print(f"Missing values after: {df['Review Rating'].isnull().sum()}")

# =============================================================================
# SECTION 3: DATA CLEANING - COLUMN NAME STANDARDIZATION
# =============================================================================
# Data cleaning is essential for downstream processing. Column names should follow
# consistent naming conventions to make the code more readable and maintainable.
# This section standardizes column names to follow Python naming conventions.

print("\n" + "=" * 60)
print("3. DATA CLEANING")
print("=" * 60)

# Display the original column names before any cleaning
# This helps us see what transformations are needed
print("\n--- Original Columns ---")
print(df.columns.tolist())

# Convert column names to snake_case (lowercase with underscores)
# This follows Python naming conventions (PEP 8 style guide)
# snake_case makes column names easier to work with in Python code
# It also makes SQL queries easier when exporting to databases
# Steps:
# 1. str.lower() - Sabhi characters ko lowercase mein convert karta hai (jaise "Age" -> "age")
# 2. str.replace(' ', '_') - Spaces ko underscore se replace karta hai
# 3. str.lower().str.replace(' ', '_') - Dono operations ek saath
# Ye Python coding standards ke according hai
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Clean specific column names that may have special characters or units
# 'purchase_amount_(usd)' contains parentheses and unit information
# We simplify this to just 'purchase_amount' for easier handling
# rename() - Column ka naam badalne ke liye use hota hai
# inplace=True - Changes ko seedha DataFrame mein save karta hai (naye variable ki zarurat nahi)
# inplace=False hota toh humein naya variable banana padta
df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'}, inplace=True)

# Display the cleaned column names
print("\n--- Cleaned Columns (snake_case) ---")
print(df.columns.tolist())

# =============================================================================
# SECTION 4: FEATURE ENGINEERING
# =============================================================================
# Feature engineering is the process of creating new features (columns) from existing data.
# This is one of the most important steps in data analysis and machine learning.
# Good features can significantly improve the quality of insights and predictions.

print("\n" + "=" * 60)
print("4. FEATURE ENGINEERING")
print("=" * 60)

# ---------------------------------------------------------------------
# 4a. Create Age Groups from Continuous Age Data
# ---------------------------------------------------------------------
# Converting continuous age values to categorical age groups makes analysis easier
# and provides meaningful segments for business insights (e.g., marketing campaigns)
# 
# Using qcut for equal-sized quantile-based bins (4 quartiles)
# qcut divides the data into n equal-sized quantile groups
# This ensures each age group has approximately the same number of customers
# which is useful for balanced comparison across groups

# Define meaningful labels for the age groups
# These labels represent different life stages and potential shopping behaviors
# labels - Ye list hai jisme hum age groups ke names rakhte hain
labels = ['Young Adults', 'Adults', 'Middle-aged', 'Seniors']

# pd.qcut() creates quantile-based bins:
# - Automatically calculates bin edges based on data distribution
# - Creates 4 bins (q=4) representing 4 quartiles (0-25%, 25-50%, 50-75%, 75-100%)
# - Assigns labels to each bin
# qcut() - Quantile-based cutting, data ko equal parts mein baata hai
# q=4 - 4 parts mein baatne ke liye (4 quartiles)
# labels - Har quartile ko naam dene ke liye
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

print("\n--- Age Group Distribution ---")
# Show count of customers in each age group, sorted by index (age order)
# value_counts() - Har unique value kitni baar aya hai ye count karta hai
# sort_index() - Alphabetically ya numerically sort karta hai
print(df['age_group'].value_counts().sort_index())
# Show sample of original age and new age_group for verification
# df[['age', 'age_group']] - Do columns select karne ka tarika
# head(10) - Pehle 10 rows dikhane ke liye
print(df[['age', 'age_group']].head(10))

# ---------------------------------------------------------------------
# 4b. Convert Purchase Frequency to Numerical Values (in days)
# ---------------------------------------------------------------------
# Purchase frequency is stored as categorical text (e.g., "Weekly", "Monthly")
# Converting to numerical days helps in:
# - Calculating customer lifetime value
# - Analyzing purchase patterns
# - Building predictive models

# Create a mapping dictionary from categorical frequency to approximate days
# These values represent the typical number of days between purchases
frequency_mapping = {
    'Fortnightly': 14,      # Every 2 weeks = 14 days
    'Weekly': 7,           # Once per week = 7 days
    'Monthly': 30,         # Once per month = 30 days (approximate)
    'Quarterly': 90,       # Every 3 months = 90 days
    'Bi-Weekly': 14,       # Same as Fortnightly = 14 days
    'Annually': 365,       # Once per year = 365 days
    'Every 3 Months': 90  # Same as Quarterly = 90 days
}

# Map the categorical frequency values to numerical days using the dictionary
# This creates a new column with numerical representation of purchase frequency
# map() - Dictionary use karke ek column ke values ko doosre values mein convert karta hai
# Yahan text ko numbers mein badal rahe hain
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

print("\n--- Purchase Frequency Mapping ---")
# Display sample of original categorical and new numerical frequency
print(df[['frequency_of_purchases', 'purchase_frequency_days']].head(10))

# ---------------------------------------------------------------------
# 4c. Check for and Remove Redundant Columns
# ---------------------------------------------------------------------
# Redundant columns consume memory and can confuse analysis
# This check identifies columns that contain identical information

# Check if 'discount_applied' and 'promo_code_used' contain the same information
# If they always have the same values, one is redundant
print("\n--- Checking for Redundant Columns ---")

# Compare both columns element-wise using ==
# .all() returns True only if ALL comparisons are True
# == - Do columns ke har row ko compare karta hai
# .all() - Agar sabhi comparisons True hain to True return karta hai
same_values = (df['discount_applied'] == df['promo_code_used']).all()
print(f"discount_applied == promo_code_used: {same_values}")

# If they're identical, drop the redundant column to simplify the dataset
if same_values:
    # axis=1 means we're dropping a column (0 would be a row)
    # axis=1 = column delete karna, axis=0 = row delete karna
    # inplace=True modifies the DataFrame directly without needing assignment
    # drop() - Column ya row delete karne ke liye use hota hai
    df.drop('promo_code_used', axis=1, inplace=True)
    print("Dropped 'promo_code_used' (redundant with 'discount_applied')")

# =============================================================================
# SECTION 5: EXPLORATORY DATA ANALYSIS (EDA) - INTERVIEW QUESTIONS
# =============================================================================
# This section answers common data analysis interview questions about customer behavior.
# Each question is designed to test different analytical skills and domain knowledge.
# EDA is the process of exploring data to discover patterns, relationships, and insights.

print("\n" + "=" * 60)
print("5. EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# =============================================================================
# Question 1: What is the average purchase amount?
# =============================================================================
# This fundamental question helps understand customer spending patterns
# We calculate both mean and median because they tell different stories:
# - Mean: Arithmetic average, sensitive to extreme values
# - Median: Middle value, robust to outliers
print("\n--- Q1: Average Purchase Amount ---")
# Calculate mean purchase amount across all transactions
# mean() - Sabhi values ka average nikalta hai (sabka jod / count)
# .2f - Do decimal places tak dikhane ke liye (formatting)
print(f"Mean: ${df['purchase_amount'].mean():.2f}")
# Calculate median purchase amount (50th percentile)
# median() - Values ko sort karke beech wala value return karta hai
# Outliers se affected nahi hota
print(f"Median: ${df['purchase_amount'].median():.2f}")

# =============================================================================
# Question 2: What is the distribution of purchases by category?
# =============================================================================
# Understanding which product categories are most popular helps with:
# - Inventory management
# - Marketing strategy
# - Product development priorities
print("\n--- Q2: Purchases by Category ---")
# value_counts() counts unique values and sorts by frequency (descending by default)
# Har category kitni baar aya hai ye count karta hai
print(df['category'].value_counts())

# =============================================================================
# Question 3: What is the average review rating by category?
# =============================================================================
# Review ratings indicate customer satisfaction. By category, this shows:
# - Which products are most/least satisfying
# - Potential areas for improvement
# - Quality perception differences across categories
print("\n--- Q3: Average Review Rating by Category ---")
# groupby() groups data by category, then mean() calculates average rating
# groupby() - Data ko kisi column ke hisaab se group karta hai
# sort_values(ascending=False) - Udaar se niche sort karta hai
print(df.groupby('category')['review_rating'].mean().sort_values(ascending=False))

# =============================================================================
# Question 4: What is the customer age distribution?
# =============================================================================
# Age distribution helps segment customers and tailor marketing:
# - Different age groups have different preferences
# - Helps in creating targeted campaigns
# - Understanding customer demographics
print("\n--- Q4: Customer Age Distribution ---")
# Find minimum, maximum, and average age in the dataset
# min() - Minimum value find karta hai
# max() - Maximum value find karta hai
# mean() - Average calculate karta hai
print(f"Min Age: {df['age'].min()}")
print(f"Max Age: {df['age'].max()}")
print(f"Mean Age: {df['age'].mean():.2f}")

# =============================================================================
# Question 5: Which payment method is most popular?
# =============================================================================
# Payment method analysis reveals:
# - Customer preferences for transaction methods
# - Potential for introducing new payment options
# - Security and convenience concerns by demographic
print("\n--- Q5: Most Popular Payment Method ---")
# Count occurrences of each payment method
# value_counts() - Har payment method kitni baar use hua hai ye batata hai
print(df['payment_method'].value_counts())

# =============================================================================
# Question 6: What is the purchase pattern by season?
# =============================================================================
# Seasonal analysis helps:
# - Plan inventory for peak seasons
# - Design seasonal promotions
# - Understand cyclical buying behavior
print("\n--- Q6: Purchases by Season ---")
# Count purchases in each season (Spring, Summer, Fall, Winter)
# value_counts() - Har season mein kitne purchases huye ye count karta hai
print(df['season'].value_counts())

# =============================================================================
# Question 7: Average purchase amount by age group
# =============================================================================
# This analysis reveals:
# - Which age groups spend the most
# - Spending power differences by life stage
# - Opportunities for age-specific marketing
print("\n--- Q7: Average Purchase Amount by Age Group ---")
# Group by age group and calculate average purchase amount
# groupby('age_group') - Age group ke hisaab se data ko group karta hai
# ['purchase_amount'].mean() - Har group ka average purchase nikalta hai
print(df.groupby('age_group')['purchase_amount'].mean())

# =============================================================================
# Question 8: Which shipping type is most preferred?
# =============================================================================
# Shipping preference analysis informs:
# - Logistics and fulfillment strategy
# - Cost optimization opportunities
# - Customer service improvements
print("\n--- Q8: Most Preferred Shipping Type ---")
# Count occurrences of each shipping type
# value_counts() - Har shipping type kitni baar use hua hai ye batata hai
print(df['shipping_type'].value_counts())

# =============================================================================
# Question 9: Subscription status impact on purchase amount
# =============================================================================
# Analyzing subscription customers vs non-subscribers:
# - Do subscribers spend more/less?
# - Is subscription model profitable?
# - Cross-selling and retention strategies
print("\n--- Q9: Subscription Status vs Purchase Amount ---")
# Group by subscription status and show average purchase amount
# groupby('subscription_status') - Subscription wale aur non-subscription wale alag karta hai
# mean() - Dono groups ka average purchase compare karta hai
print(df.groupby('subscription_status')['purchase_amount'].mean())

# =============================================================================
# Question 10: Top locations by total purchase amount
# =============================================================================
# Geographic analysis helps:
# - Regional marketing campaigns
# - Store location decisions
# - Distribution and logistics planning
print("\n--- Q10: Top 5 Locations by Total Purchase Amount ---")
# Group by location, sum purchase amounts, show top 5
# groupby('location') - Har location ke liye alag karta hai
# sum() - Har location ka total purchase amount add karta hai
# sort_values(ascending=False) - Sabse zyada se kam dikhata hai
# head() - Sirf top 5 dikhata hai
print(df.groupby('location')['purchase_amount'].sum().sort_values(ascending=False).head())

# =============================================================================
# SECTION 6: DATA EXPORT
# =============================================================================
# After all processing and analysis, we export the cleaned dataset
# This cleaned data can be used for further analysis, reporting, or ML models

print("\n" + "=" * 60)
print("6. DATA EXPORT")
print("=" * 60)

# Save the cleaned and processed data to a new CSV file
# index=False prevents pandas from writing row indices to the CSV
# The cleaned dataset now has:
# - Missing values handled
# - Standardized column names
# - Additional engineered features
df.to_csv('customer_shopping_cleaned.csv', index=False)
# to_csv() - DataFrame ko CSV file mein save karta hai
# index=False - Row numbers CSV mein nahi likhega, sirf data likhega
print("\nCleaned data saved to 'customer_shopping_cleaned.csv'")

# Print final DataFrame information to confirm the final state
print("\n--- Final DataFrame Info ---")
# Show final shape (number of rows and columns)
# shape - DataFrame kitne rows aur columns ka hai ye batata hai (rows, columns)
print(f"Shape: {df.shape}")
# Show final columns
# columns.tolist() - Saare column names ki list return karta hai
print(f"Columns: {df.columns.tolist()}")
# Verify no missing values remain
# sum() of sum of all null values - Total kitne missing values bache hain
print(f"Remaining missing values: {df.isnull().sum().sum()}")



#to connect to database and export data
import psycopg2

try:
    conn = psycopg2.connect(
    host="localhost",
    database="customer_behavior_analysis",
    user="postgres",
    password="1234",
    port="5432"
)
    

    print("Connection Successful 🚀")

    cur = conn.cursor()
    cur.execute("SELECT current_database();")
    print("Connected to:", cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/customer_behavior_analysis"
)

df.to_sql("customer_data", engine, if_exists="replace", index=False)

print("Data uploaded successfully 🚀")