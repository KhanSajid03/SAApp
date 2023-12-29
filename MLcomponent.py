import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from stock import sendUserInput
#code from Sahaj Godhani Article in Medium
#URL: https://sahajgodhani777.medium.com/stock-recommendations-from-yahoo-finance-using-ml-models-in-python-3f3e8c232c38 
symbol = sendUserInput()
stock_data = yf.download(symbol, start='2022-01-05', end='2023-01-06')

# Creating a DataFrame and calculating daily returns
df = pd.DataFrame(stock_data)
df['DailyReturn'] = df['Close'].pct_change()
df['Target'] = (df['DailyReturn'] > 0).astype(int)  # Binary classification: 1 if positive, 0 if not

# Dropping rows with missing values
df = df.dropna()

# Selecting features and target variable
features = ['Open', 'High', 'Low', 'Close', 'Volume']
X = df[features]
y = df['Target']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Creating a DataFrame for actual vs. predicted values
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# Plotting actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.plot(predictions_df.index, predictions_df['Actual'], label='Actual', marker='o')
plt.plot(predictions_df.index, predictions_df['Predicted'], label='Predicted', linestyle='dashed', marker='x')
plt.xlabel('Date')
plt.ylabel('Target (1: Positive, 0: Negative)')
plt.title('Actual vs. Predicted Stock Daily Returns')
plt.legend()
plt.grid(True)
plt.show()