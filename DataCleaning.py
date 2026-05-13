import numpy as np
import pandas as pd

data = {
    'Name': ['Gaurav', 'Guddu', 'Ravi', 'Ram', 'Mohit', np.nan] * 1000,
    'Age': [35, 28, 42, 50, 45, np.nan] * 1000,
    'Salary': [60000, 75000, 90000, 120000, 200000, 1500000] * 1000,
    'Department_ID': [101, 102, 103, 104, 105, 106] * 1000
}

df = pd.DataFrame(data)

print(df.head())
# print(df)


def data_cleaning():
    # Count missing values column-wise
    missing_values = df.isnull().sum()
    print(f"Missing Values: {missing_values}")

    # Percentage of null values
    null_percent = df.isnull().sum() / df.shape[0] * 100
    print(f"Null Percent: {null_percent}")

    # Fill missing values
    df['Name'] = df['Name'].fillna('Unknown')
    df['Age'] = df['Age'].fillna(df['Age'].median())

    # Check again
    print(df.isnull().sum())

data_cleaning()