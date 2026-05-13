import pandas as pd
import numpy as np

data = {
    'ID': [1, 2, 3, 4, 5, 2, 6],
    'Name': ['Alaukik Nandan', 'Prabhat Kumar', 'Avinash', 
             'Adarsh Mishra', 'Lekhika ', 'Prabhat Kumar', 'Keshav'],
    'Age': [26, 25, 'Unknown', 24, 24, 25, 19],
    'Salary': [50000, 60000, 70000, 'N/A', 90000, 60000, 100000]
}

df = pd.DataFrame(data)

print("Original Dataset with Inconsistencies and Duplicates:")
print(df)
print()

# Convert to numeric (handle errors)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Fill missing values using median
median_age = df['Age'].median()
print(f"Median Age: {median_age}")
df['Age'] = df['Age'].fillna(median_age)

median_salary = df['Salary'].median()
print(f"Median Salary: {median_salary}")
df['Salary'] = df['Salary'].fillna(median_salary)

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Dataset without Inconsistencies and Duplicates:")
print(df)
