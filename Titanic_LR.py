from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

train = pd.read_csv("../Python Sample Dataset/titanic_train.csv")
test = pd.read_csv("../Python Sample Dataset/titanic_test.csv")

print(train)

# Convert categorical → numeric
train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})

# Fill missing values
train['Age'] = train['Age'].fillna(train['Age'].median())
test['Age'] = test['Age'].fillna(test['Age'].median())

train['Fare'] = train['Fare'].fillna(train['Fare'].median())
test['Fare'] = test['Fare'].fillna(test['Fare'].median())

# Fill Embarked
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])
test['Embarked'] = test['Embarked'].fillna(test['Embarked'].mode()[0])

train['Embarked'] = train['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
test['Embarked'] = test['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

X_train = train[features]
y_train = train['Survived']

X_test = test[features]

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_pred_binary = (y_pred > 0.5).astype(int)

y_train_pred = model.predict(X_train)
y_train_binary = (y_train_pred > 0.5).astype(int)

train_accuracy = accuracy_score(y_train, y_train_binary)
print("Training Accuracy:", train_accuracy)

results = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Survived': y_pred_binary,
    'Raw_Score': y_pred.round(3)   # the original regression output before thresholding
})

results['Outcome'] = results['Survived'].map({0: 'Did NOT survive', 1: 'Survived'})

print("\nSurvival prediction counts:")
print(results['Survived'].value_counts())

print("\nFirst 15 predictions:")
print(results[['PassengerId', 'Raw_Score', 'Survived', 'Outcome']].head(100).to_string(index=False))

sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 6))
ax1 = axes[0, 0]
counts = pd.Series(y_pred_binary).value_counts().sort_index()
bars = ax1.bar(['Did NOT Survive (0)', 'Survived (1)'], counts.values,
               color=['#e74c3c', '#2ecc71'], edgecolor='black')
ax1.set_title("Predicted Survival Counts (Test Set)", fontweight='bold')
ax1.set_ylabel("Number of Passengers")
for bar in bars:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
             int(bar.get_height()), ha='center', fontweight='bold')

ax2 = axes[0, 1]
ax2.hist(y_pred, bins=30, color='#3498db')
ax2.set_title("Distribution of Raw Regression Scores", fontweight='bold')
ax2.set_xlabel("Predicted Score")
ax2.set_ylabel("Frequency")
ax2.legend()

ax3 = axes[1, 0]
cm = confusion_matrix(y_train, y_train_binary)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Pred: Died', 'Pred: Survived'],
            yticklabels=['Actual: Died', 'Actual: Survived'], ax=ax3)
ax3.set_title(f"Confusion Matrix — Train (Acc: {train_accuracy:.3f})",
              fontweight='bold')

ax4 = axes[1, 1]
test_results = test.copy()
test_results ['Predicted']=y_pred_binary

class_survival = test_results.groupby('Pclass')['Predicted'].mean()
bars = ax4.bar([f"Class {c}" for c in class_survival.index],
               class_survival.values,
               color=['#f1c40f', '#e67e22', '#95a5a6'], edgecolor='black')

ax4.set_title("Predicted Survival Rate by Pclass", fontweight='bold')
ax4.set_ylabel("Survival Rate")

for bar in bars:
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
             f"{bar.get_height():.2%}", ha='center', fontweight='bold')


plt.title("Sorted Raw Regression Scores per Test Passenger")
plt.xlabel("Passenger (sorted by score)")
plt.ylabel("Predicted Score")
plt.legend()
plt.tight_layout()
plt.show()

def logistic_reg():

    def impute_age(cols):
        Age = cols.iloc[0]
        Pclass = cols.iloc[1]

        if pd.isnull(Age):
            if Pclass == 1:
                return 37
            elif Pclass == 2:
                return 29
            else:
                return 24
        else:
            return Age

    train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)

    train.drop('Cabin', axis=1, inplace=True)
    print(train.head())
    print(train.info())

    print(pd.get_dummies(train['Embarked'], drop_first=True).head())

    sex = pd.get_dummies(train['Sex'])
    embark=pd.get_dummies(train['Embarked'],drop_first=True)
    print(pd.get_dummies(train['Embarked'], drop_first=True).head())

    # drop columns that are not required or that don't have enough data
    train.drop(['Embarked', 'Name', 'Ticket'], axis=1, inplace=True)

    # display top records
    train.head()

    train = pd.concat([train, sex, embark], axis=1)


# ============================= EXERCISE ===================================


def logistic_regression():
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score

    def Logistic(X, y):
        print("\n-------------------LOGISTIC REGRESSION------------------------\n")
        log_baseline = LogisticRegression(max_iter=1000)
        log_baseline.fit(X, y)
        
        base_train_acc = accuracy_score(y, log_baseline.predict(X))
        base_cv_acc = cross_val_score(log_baseline, X, y, cv=5, scoring='accuracy').mean()
        
        print(f"Baseline Training Accuracy : {base_train_acc:.4f}")
        print(f"Baseline 5-Fold CV Accuracy: {base_cv_acc:.4f}")
        return base_cv_acc

    def Transforming():
        print("\n ------------TRANSFORMATION-----------------\n")
        
        train_eng = pd.read_csv("../Python Sample Dataset/titanic_train.csv")
        test_eng = pd.read_csv("../Python Sample Dataset/titanic_test.csv")
        datasets = [train_eng, test_eng]
        
        for data in datasets:
            data['Title'] = data['Name'].replace(['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr', 
                                                   'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
            data['Title'] = data['Title'].replace(['Mlle', 'Ms'], 'Miss')
            data['Title'] = data['Title'].replace('Mme', 'Mrs')
            title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
            data['Title'] = data['Title'].map(title_mapping).fillna(0)
            
            data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
            data['IsAlone'] = 1
            data.loc[data['FamilySize'] > 1, 'IsAlone'] = 0
            
            data['Sex'] = data['Sex'].map({'male': 0, 'female': 1}).astype(int)
            
            data['Age'] = data['Age'].fillna(data.groupby('Title')['Age'].transform('median'))
            data.loc[data['Age'] <= 16, 'Age'] = 0
            data.loc[(data['Age'] > 16) & (data['Age'] <= 32), 'Age'] = 1
            data.loc[(data['Age'] > 32) & (data['Age'] <= 48), 'Age'] = 2
            data.loc[(data['Age'] > 48) & (data['Age'] <= 64), 'Age'] = 3
            data.loc[data['Age'] > 64, 'Age'] = 4
            
            data['Embarked'] = data['Embarked'].fillna(train_eng['Embarked'].mode()[0])
            data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)
            
            data['Fare'] = data['Fare'].fillna(train_eng['Fare'].median())
            data.loc[data['Fare'] <= 7.91, 'Fare'] = 0
            data.loc[(data['Fare'] > 7.91) & (data['Fare'] <= 14.454), 'Fare'] = 1
            data.loc[(data['Fare'] > 14.454) & (data['Fare'] <= 31), 'Fare'] = 2
            data.loc[data['Fare'] > 31, 'Fare'] = 3
            data['Fare'] = data['Fare'].astype(int)

        features_eng = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Title', 'FamilySize', 'IsAlone']
        print("New Features Extracted:", features_eng)
        
        return train_eng[features_eng], train_eng['Survived'], test_eng[features_eng]

    def difference(X, y, baseline_cv_acc):
        print("\n----------------PERF--------------------\n")
        
        log_improved = LogisticRegression(max_iter=1000)
        log_improved.fit(X, y)
        
        imp_train_acc = accuracy_score(y, log_improved.predict(X))
        imp_cv_acc = cross_val_score(log_improved, X, y, cv=5, scoring='accuracy').mean()
        
        print(f"Improved Training Accuracy : {imp_train_acc:.4f}")
        print(f"Improved 5-Fold CV Accuracy: {imp_cv_acc:.4f}")
        print(f"\n---> Absolute CV Improvement: {(imp_cv_acc - baseline_cv_acc)*100:.2f}% <---")

    
    baseline_cv = Logistic(X_train, y_train)
    X_train_eng, y_train_eng, X_test_eng = Transforming()
    difference(X_train_eng, y_train_eng, baseline_cv)

logistic_regression()