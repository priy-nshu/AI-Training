# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# ============================================
# 1. LOAD AND EXPLORE DATA
# ============================================
housing = pd.read_csv("../Python Sample Dataset/housing.csv")

print("="*60)
print("DATASET OVERVIEW")
print("="*60)
print(f"Dataset shape: {housing.shape}")
print(f"\nFirst few rows:")
print(housing.head())
print(f"\nData types:\n{housing.dtypes}")
print(f"\nMissing values:\n{housing.isnull().sum()}")
print(f"\nStatistical Summary:\n{housing.describe()}")

# ============================================
# 2. DATA PREPROCESSING
# ============================================
print("\n" + "="*60)
print("DATA PREPROCESSING")
print("="*60)

# Separate features and target
X = housing.drop("median_house_value", axis=1)
y = housing["median_house_value"]

# Handle categorical variables
print(f"\nCategorical columns: {X.select_dtypes(include=['object']).columns.tolist()}")
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
print(f"\nFilling missing values with median...")
X = X.fillna(X.median())

print(f"Features shape after preprocessing: {X.shape}")
print(f"Target shape: {y.shape}")

# ============================================
# 3. FEATURE SCALING (IMPORTANT FOR INTERPRETATION)
# ============================================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# ============================================
# 4. TRAIN-TEST SPLIT
# ============================================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print(f"\nTrain set size: {X_train.shape[0]}")
print(f"Test set size: {X_test.shape[0]}")

# ============================================
# 5. TRAIN LINEAR REGRESSION MODEL
# ============================================
print("\n" + "="*60)
print("MODEL TRAINING")
print("="*60)

model = LinearRegression()
model.fit(X_train, y_train)

# ============================================
# 6. MAKE PREDICTIONS
# ============================================
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# ============================================
# 7. MODEL EVALUATION
# ============================================
print("\n" + "="*60)
print("MODEL PERFORMANCE METRICS")
print("="*60)

# Training metrics
train_mse = mean_squared_error(y_train, y_train_pred)
train_rmse = np.sqrt(train_mse)
train_mae = mean_absolute_error(y_train, y_train_pred)
train_r2 = r2_score(y_train, y_train_pred)

# Testing metrics
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_mae = mean_absolute_error(y_test, y_test_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"\nTRAINING SET METRICS:")
print(f"  MSE:  ${train_mse:,.2f}")
print(f"  RMSE: ${train_rmse:,.2f}")
print(f"  MAE:  ${train_mae:,.2f}")
print(f"  R²:   {train_r2:.4f}")

print(f"\nTEST SET METRICS:")
print(f"  MSE:  ${test_mse:,.2f}")
print(f"  RMSE: ${test_rmse:,.2f}")
print(f"  MAE:  ${test_mae:,.2f}")
print(f"  R²:   {test_r2:.4f}")

# Cross-validation score
cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
print(f"\nCROSS-VALIDATION R² SCORES:")
print(f"  Scores: {cv_scores}")
print(f"  Mean: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# ============================================
# 8. FEATURE IMPORTANCE
# ============================================
print("\n" + "="*60)
print("FEATURE COEFFICIENTS (Importance)")
print("="*60)

coefficients_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_,
    "Abs_Coefficient": np.abs(model.coef_)
}).sort_values("Abs_Coefficient", ascending=False)

print(f"\nIntercept: {model.intercept_:,.2f}")
print(f"\nTop 10 Most Important Features:")
print(coefficients_df.head(10).to_string(index=False))

# ============================================
# 9. VISUALIZATIONS
# ============================================
fig, axes = plt.subplots(2, 2, figsize=(12, 5))
fig.suptitle('Linear Regression Analysis - Housing Data', fontsize=16, fontweight='bold')

# 1. Actual vs Predicted (Test Set)
ax1 = axes[0, 0]
ax1.scatter(y_test, y_test_pred, alpha=0.6, color='blue', edgecolors='k')
ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
ax1.set_xlabel("Actual Prices ($)")
ax1.set_ylabel("Predicted Prices ($)")
ax1.set_title(f"Actual vs Predicted (Test Set)\nR² = {test_r2:.4f}")
ax1.grid(True, alpha=0.3)

# 2. Residuals Plot
ax2 = axes[0, 1]
residuals = y_test - y_test_pred
ax2.scatter(y_test_pred, residuals, alpha=0.6, color='green', edgecolors='k')
ax2.axhline(y=0, color='r', linestyle='--', lw=2)
ax2.set_xlabel("Predicted Prices ($)")
ax2.set_ylabel("Residuals ($)")
ax2.set_title("Residuals Plot")
ax2.grid(True, alpha=0.3)

# 3. Feature Importance
ax3 = axes[1, 0]
top_features = coefficients_df.head(10)
colors = ['green' if x > 0 else 'red' for x in top_features['Coefficient']]
ax3.barh(top_features['Feature'], top_features['Coefficient'], color=colors)
ax3.set_xlabel("Coefficient Value")
ax3.set_title("Top 10 Feature Importance")
ax3.grid(True, alpha=0.3, axis='x')

# 4. Distribution of Residuals
ax4 = axes[1, 1]
ax4.hist(residuals, bins=30, color='purple', alpha=0.7, edgecolor='black')
ax4.set_xlabel("Residuals ($)")
ax4.set_ylabel("Frequency")
ax4.set_title(f"Distribution of Residuals\nMean = {residuals.mean():.2f}, Std = {residuals.std():.2f}")
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# ============================================
# 10. ADDITIONAL ANALYSIS
# ============================================
print("\n" + "="*60)
print("RESIDUAL ANALYSIS")
print("="*60)
print(f"Mean of Residuals: {residuals.mean():.2f} (should be ≈ 0)")
print(f"Std Dev of Residuals: {residuals.std():.2f}")
print(f"Min Residual: {residuals.min():.2f}")
print(f"Max Residual: {residuals.max():.2f}")

# ============================================
# 11. MODEL SUMMARY
# ============================================
print("\n" + "="*60)
print("MODEL SUMMARY")
print("="*60)
print(f"Number of Features: {len(X.columns)}")
print(f"Training Samples: {len(X_train)}")
print(f"Testing Samples: {len(X_test)}")
print(f"\nModel Equation (simplified):")
print(f"Price = {model.intercept_:,.2f} + ", end="")
print(" + ".join([f"{coef:.4f}*{feat}" for feat, coef in zip(X.columns[:3], model.coef_[:3])]) + " + ...")