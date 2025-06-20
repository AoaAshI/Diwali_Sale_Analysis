import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Basic info
print(df.shape)
print(df.head())
print(df.info())

# Data Cleaning
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)  # Fixed True
print(pd.isnull(df).sum())  # Fixed typo

df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype(int)  # No quotes needed for int

# Column renaming
df.rename(columns={'Marital_Status':'Married'}, inplace=True)  # Inplace=True
print(df.columns)

# Descriptive statistics
print(df.describe())
print(df[['Age', 'Orders', 'Amount']].describe())

# Visualization 1: Gender count
ax = sns.countplot(x='Gender', data=df, hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)

# Sales based on Gender
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gen, hue='Gender')

# Visualization 2: Age group
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)

# Sales by Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)

# Top 10 States by Orders
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Orders')

# Top 10 States by Amount
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Amount')

# Marital Status count
ax = sns.countplot(data=df, x='Married')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)

# Sales by Marital Status and Gender
sales_state = df.groupby(['Married', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_state, x='Married', y='Amount', hue='Gender')

# Occupation count
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)

# Sales by Occupation
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_state, x='Occupation', y='Amount')

# Product Category count
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)

# Top 10 Product Categories by Amount
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_state, x='Product_Category', y='Amount')

# Top 10 Products by Orders
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_ID', y='Orders')

# Top 10 Products by Orders (using barplot)
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.show()
