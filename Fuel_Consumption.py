import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split

# Load the file and display top few records
data = pd.read_csv("../Python Sample Dataset/Fuel_consumption_2000-2022.csv")
print(data.head())
print(data.tail())  # last 10

# Some details about the dataframe
print(f"\nColumn heading\n", data.columns)        # name of columns
print(f"\nNo. of columns: {data.columns.size}")   # num of columns
print(data.shape)

# Summarize the data
print(data.describe().transpose())

# Check the data types
print("\n Data Types:",data.dtypes)

corr=data.corr(numeric_only=True)
print("\nCo-Relation:\n",corr)

print(data[0:0:13])

print("nulls",data.isnull().sum())

# split the data into training and testing sets

data.columns = data.columns.str.strip()
data = data.select_dtypes(include=[np.number])

train = data.drop(['EMISSIONS'], axis=1)
test = data['EMISSIONS']

X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.2, random_state=42)

print(f"Shape of training data: {train.shape}, Testing data: {test.shape}")

# train the model and find the coefficients for best fit
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

# print the coefficients
print("Coefficient ", regr.coef_)
print("Intercept ", regr.intercept_)

# run the prediction
pred = regr.predict(X_test)

print(type(pred), type(y_test))

# display accuracy metrics
print("Mean of absolutes %0.3f" % np.mean(np.absolute(pred - y_test)))
print("Mean sum of squares %0.3f" % (np.mean((pred - y_test) ** 2)))

# Mean Squared Error
MSE = np.square(np.subtract(pred, y_test)).mean()
print("R2 Score - %.2f" % (r2_score(y_test, pred)))
print(pred)