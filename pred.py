# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv('Admission_Predict.csv')

# print("Column Names:")
# print(data.columns)

# print("\nPreview of Data (First 5 Rows):")
# print(data.head())


# x_column = 'GRE Score'       # Example: Independent variable
# y_column = 'Chance of Admit ' # Example: Dependent variable

# plt.figure(figsize=(10, 6))
# plt.scatter(data[x_column], data[y_column], color='blue', alpha=0.7, label=f'{x_column} vs {y_column}')
# plt.title(f'{x_column} vs {y_column}', fontsize=16)
# plt.xlabel(x_column, fontsize=14)
# plt.ylabel(y_column, fontsize=14)
# plt.grid(True)
# plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Admission_Predict.csv')

# Renaming columns for simplicity if needed
data.rename(columns={'GRE Score': 'GRE_Score', 'Chance of Admit ': 'Chance_of_Admit'}, inplace=True)

# Summary Statistics
print("Summary Statistics:")
print(data[['GRE_Score', 'Chance_of_Admit']].describe())

# Correlation
correlation = data[['GRE_Score', 'Chance_of_Admit']].corr().iloc[0, 1]
print(f"\nCorrelation between GRE Score and Chance of Admit: {correlation:.2f}")

# Histogram for GRE Scores
plt.figure(figsize=(10, 6))
sns.histplot(data['GRE_Score'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of GRE Scores', fontsize=16)
plt.xlabel('GRE Score', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)
plt.show()

# Scatterplot with Trendline
plt.figure(figsize=(10, 6))
sns.regplot(x='GRE_Score', y='Chance_of_Admit', data=data, color='blue', line_kws={"color": "red"})
plt.title('GRE Score vs Chance of Admission (with Trendline)', fontsize=16)
plt.xlabel('GRE Score', fontsize=14)
plt.ylabel('Chance of Admit', fontsize=14)
plt.grid(True)
plt.show()

# Group Insights
bins = [0, 300, 320, 340]
labels = ['Low (0-300)', 'Medium (301-320)', 'High (321-340)']
data['GRE_Category'] = pd.cut(data['GRE_Score'], bins=bins, labels=labels)

grouped_data = data.groupby('GRE_Category')['Chance_of_Admit'].mean().reset_index()
print("\nAverage Chance of Admission by GRE Category:")
print(grouped_data)

# Bar Plot for Group Insights
plt.figure(figsize=(10, 6))
sns.barplot(x='GRE_Category', y='Chance_of_Admit', data=grouped_data, palette='viridis')
plt.title('Average Chance of Admission by GRE Category', fontsize=16)
plt.xlabel('GRE Category', fontsize=14)
plt.ylabel('Average Chance of Admission', fontsize=14)
plt.grid(True)
plt.show()
