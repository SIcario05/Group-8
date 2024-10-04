import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set the title of the app
st.title('Laptop Price Analysis Dashboard')

# Load dataset
df = pd.read_csv('laptop_price - dataset.csv')

# 1. Dataset Overview
st.header("Dataset Overview")

st.subheader("First 5 rows of the dataset:")
st.write(df.head())  # Display the first 5 rows of the dataset

st.subheader("Dataset Information:")
buffer = pd.DataFrame(df.dtypes).rename(columns={0: 'Data Type'})
st.write(buffer)

st.subheader("Descriptive Statistics:")
st.write(df.describe())  # Summary statistics

st.subheader("Missing Values in the Dataset:")
st.write(df.isna().sum())  # Check for missing values

# Value counts for the 'Company' column (example)
st.subheader("Count of Laptops by Company (All):")
company_counts = df['Company'].value_counts()  # Count the unique values in the 'Company' column
st.write(company_counts)

# Filter only those with even counts
st.subheader("Count of Laptops by Company (Even Occurrences):")
even_company_counts = company_counts[company_counts % 2 == 0]
st.write(even_company_counts)

# Graph 1: Histogram
st.subheader('Graph 1: Distribution of Laptop Prices in Euro')
plt.figure(figsize=(10, 6))
sns.histplot(df['Price (Euro)'], bins=20, kde=True, color='blue')
plt.title('Distribution of Laptop Prices in Euro')
plt.xlabel('Price (Euro)')
plt.ylabel('Frequency')
st.pyplot(plt)

# Graph 2: Scatter Plot
st.subheader('Graph 2: Laptop Price vs. RAM (GB)')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='RAM (GB)', y='Price (Euro)', hue='Company', palette='Set2')
plt.title('Laptop Price vs. RAM (GB)')
plt.xlabel('RAM (GB)')
plt.ylabel('Price (Euro)')
st.pyplot(plt)

# Graph 3: Box Plot
st.subheader('Graph 3: Laptop Prices by Company')
df.rename(columns={'Price (Euro)': 'Price_Euro'}, inplace=True)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Company', y='Price_Euro')
plt.title('Laptop Prices by Company')
plt.xlabel('Company')
plt.ylabel('Price (Euro)')
plt.xticks(rotation=45)
st.pyplot(plt)

# Graph 4: Heatmap
st.subheader('Graph 4: Correlation Heatmap')
plt.figure(figsize=(8, 6))
corr_matrix = df[['Inches', 'CPU_Frequency (GHz)', 'RAM (GB)', 'Weight (kg)', 'Price_Euro']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
st.pyplot(plt)

# Graph 5: Pie Chart (Plotly)
st.subheader('Graph 5: Top 19 Laptop Products by Count')
Product = df.Product.value_counts().reset_index(name='Product_count').iloc[:19]
fig = px.pie(
    data_frame=Product,
    names='Product', values='Product_count',
    hole=.1,
    color_discrete_sequence=px.colors.sequential.RdBu,
    height=600, width=1000
)
fig.update_traces(textposition='inside', textinfo='label+value')
fig.update_layout(title="Top 19 Laptop Products by Count")
st.plotly_chart(fig)

# Graph 6: Horizontal Bar Chart
st.subheader('Graph 6: Distribution of Laptop Types')
df.groupby('TypeName').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right']].set_visible(False)
plt.xlabel('Count of Laptops')
plt.ylabel('Laptop Type')
plt.title('Distribution of Laptop Types')
plt.gcf().set_size_inches(11, 6)
st.pyplot(plt)

# Graph 7: Violin Chart
st.subheader('Graph 7: RAM Distribution by Laptop Type')
plt.figure(figsize=(12, 6))
sns.violinplot(x='TypeName', y='RAM (GB)', data=df, palette='Set2', hue='TypeName')
plt.title('RAM Distribution by Laptop Type')
plt.xlabel('Laptop Type')
plt.ylabel('RAM (GB)')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# Graph 8: Bar Chart
st.subheader('Graph 8: Count of Laptops by Type')
plt.figure(figsize=(12, 6))
sns.countplot(x='TypeName', data=df, palette='Set2', hue='TypeName')
plt.title('Count of Laptops by Type')
plt.xlabel('Laptop Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)
