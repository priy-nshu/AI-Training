import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv("../Python Sample Dataset/Iris.csv")

print(df.head())      # top 10 (actually default is 5)
print(df.tail())      # last 10 (default 5)
print(df[100:110])    # rows from index 100 to 109

# Understand the dataset
print(df.describe())  # get statistics of all numerical columns
print(df.info())      # display data types and column headings

# Some details about the dataframe
print(f"\nColumn heading\n", df.columns)      # names of columns
print(f"\nNo. of columns: {df.columns.size}") # number of columns
print(f"\nShape of Dataframe: {df.shape}")

# Unique Targets
species = df['Species'].unique()
print(f"\nNo. of Unique Species: {species}")
print(f"\nRecords of each Species: {df['Species'].value_counts()}\n")

# check if there are any null values in any column
print(f"Sum of Nulls in columns: {df.isnull().sum()}")

# Pre-processing - Data Cleaning
specific_data = df[["Id", "Species"]]   # view specific column details
print("Specific Data:\n",specific_data)
print()

# drop Id col as it is not needed
df = df.drop(columns=['Id'])

# separate out the species col (name of flower) and data
Y = df['Species']
X = df.drop(columns=['Species'])

# global variables for the different models
accuracy_train_lr = accuracy_test_lr = 0.0
accuracy_train_dt = accuracy_test_dt = 0.0
accuracy_train_nb = accuracy_test_nb = 0.0
accuracy_train_knn = accuracy_test_knn = 0.0

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,train_size=0.8,random_state=42,stratify=Y)
print(x_train,x_test,y_train,y_test)


def logistic_reg():
    print("-------------------------------------LOGISTIC REG----------------------------------------------") 
    global accuracy_train_lr,accuracy_test_lr

    model_lr=LogisticRegression()

    model_lr.fit(x_train,y_train)

    result_train_lr=model_lr.predict(x_train)
    result_test_lr=model_lr.predict(x_test)

    from sklearn.metrics import accuracy_score, classification_report
    accuracy_train_lr = accuracy_score(result_train_lr, y_train)
    accuracy_test_lr = accuracy_score(result_test_lr, y_test)

    print(accuracy_train_lr)
    print(accuracy_test_lr)

    print(f"Training Result : {classification_report(result_train_lr, y_train)}")

    accuracy_test_lr = accuracy_score(result_test_lr, y_test)

    print(f"Accuracy of test: {accuracy_test_lr}")

    print(f"Test Result : {classification_report(result_test_lr, y_test)}")

print("\nDecision tree\n")


def decision_tree():
    print("-------------------------------------DECISION TREE----------------------------------------------") 
    global accuracy_train_dt, accuracy_test_dt

    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score, classification_report

    model_dt = DecisionTreeClassifier()

    model_dt.fit(x_train, y_train)

    result_train_dt = model_dt.predict(x_train)
    result_test_dt = model_dt.predict(x_test)

    print(result_train_dt)
    print(result_test_dt)

    accuracy_train_dt = accuracy_score(result_train_dt, y_train)
    print(f"Training Accuracy Score:\n {accuracy_train_nb}")
    print(f"Training Classification Report\n {classification_report(result_train_dt, y_train)}")

    accuracy_test_dt = accuracy_score(result_test_dt, y_test)
    print(f"Training Accuracy Score:\n",accuracy_test_nb)
    print(f'Testing Classification Report:\n',classification_report(result_test_dt, y_test))


 
def naive_bayes():
    print("-------------------------------------NAIVE BAYES----------------------------------------------")
    global accuracy_train_nb, accuracy_test_nb

    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score, classification_report

    model_nb = GaussianNB()
    model_nb.fit(x_train, y_train)

    result_train_nb = model_nb.predict(x_train)
    result_test_nb = model_nb.predict(x_test)

    accuracy_train_nb = accuracy_score(result_train_nb, y_train)
    print(f"Training Accuracy Score:\n {accuracy_train_nb}")
    print(f"Training Classification Report\n {classification_report(result_train_nb, y_train)}")

    accuracy_test_nb = accuracy_score(result_test_nb, y_test)
    print(f"Training Accuracy Score:\n",accuracy_test_nb)
    print(f'Testing Classification Report:\n',classification_report(result_test_nb, y_test))


def knn():
    print("-------------------------------------KNN----------------------------------------------") 
    global accuracy_train_knn, accuracy_test_knn

    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score, classification_report

    model_nb = GaussianNB()
    model_nb.fit(x_train, y_train)

    result_train_knn = model_nb.predict(x_train)
    result_test_knn = model_nb.predict(x_test)

    accuracy_train_knn = accuracy_score(result_train_knn, y_train)
    print(f"Training Accuracy Score:\n {accuracy_train_knn}")
    print(f"Training Classification Report\n {classification_report(result_train_knn, y_train)}")

    accuracy_test_knn = accuracy_score(result_test_knn, y_test)
    print(f"Training Accuracy Score:\n",accuracy_test_knn)
    print(f'Testing Classification Report:\n',classification_report(result_test_knn, y_test))


def comparison():
    print("-------------------------------------COMPARISION----------------------------------------------")
    data = {
        "Model": ["Logistic Regression", "Decision Tree", "Naive Bayes", "k-NN"],

        "Train Accuracy": [
            accuracy_train_lr * 100,
            accuracy_train_dt * 100,
            accuracy_train_nb * 100,
            accuracy_train_knn * 100
        ],

        "Test Accuracy": [
            accuracy_test_lr * 100,
            accuracy_test_dt * 100,
            accuracy_test_nb * 100,
            accuracy_test_knn * 100
        ]
    }

    df_comparison = pd.DataFrame(data)

    df_comparison["Overfit_Diff"] = (
        df_comparison["Train Accuracy"] - df_comparison["Test Accuracy"]
    )

    df_final = df_comparison.set_index("Model").T
    print(df_final)

####################################################################
logistic_reg()
decision_tree()
naive_bayes()
knn()
comparison()
