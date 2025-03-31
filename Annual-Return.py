import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


# Function to calculate expected annualized return
def calculate_annualized_return(ticker, start_date, end_date):
    # Step 1: Download historical price data
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']

    # Step 2: Calculate daily returns
    daily_returns = data.pct_change().dropna()

    # Step 3: Calculate the average daily return
    average_daily_return = daily_returns.mean()

    # Step 4: Calculate the expected annualized return
    trading_days = 252  # Assuming 252 trading days in a year
    annualized_return = (1 + average_daily_return) ** trading_days - 1

    return annualized_return


# Parameters
start_date = "2023-08-31"
end_date = "2024-08-31"

# List of tickers
tickers = ["MSFT", "PG", "DIS", "UNH", "VZ"]
annualized_returns = []

# Calculate and store annualized returns for each ticker
for ticker in tickers:
    annualized_return = calculate_annualized_return(ticker, start_date, end_date)
    annualized_returns.append(annualized_return * 100)  # Convert to percentage

# Colors for each bar
colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#d62728']  # Matching previous chart colors

# Plotting the results
x = np.arange(len(tickers))  # the label locations

plt.figure(figsize=(12, 8))

# Bar chart with different colors
plt.bar(x, annualized_returns, color=colors, width=0.4, label='Annualized Return (Bar)')

# Line chart
plt.plot(x, annualized_returns, marker='o', linestyle='-', color='red', markersize=8, label='Annualized Return (Line)')

# Adding text labels for each bar/point
for i, value in enumerate(annualized_returns):
    plt.text(i, value + 0.5, f"{value:.2f}%", ha='center', fontsize=12)

# Adding title and labels
plt.title("Expected Annualized Returns (2023-2024)", fontsize=16)
plt.xlabel("Company Ticker", fontsize=14)
plt.ylabel("Annualized Return (%)", fontsize=14)
plt.ylim(0, max(annualized_returns) + 5)  # Adjust y-axis for better visualization

# X-axis labels
plt.xticks(x, tickers)

# Adding grid and legend
plt.grid(True)
plt.legend()

# Show plot
plt.show()
