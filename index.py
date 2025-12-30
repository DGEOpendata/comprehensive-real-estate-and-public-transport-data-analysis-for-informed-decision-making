python
import pandas as pd
import matplotlib.pyplot as plt

# Load Real Estate Transactions Data
real_estate_data = pd.read_csv('abu_dhabi_real_estate_transactions.csv')

# Load Public Transport Ridership Data
public_transport_data = pd.read_csv('abu_dhabi_public_transport_ridership.csv')

# Merge datasets on 'Date' for correlation analysis
merged_data = pd.merge(real_estate_data, public_transport_data, on='Date')

# Analyze trends in property transactions vs. public transport ridership
correlation = merged_data[['Transaction Value (AED)', 'Daily Ridership']].corr()
print("Correlation between Real Estate Transactions and Public Transport Ridership:")
print(correlation)

# Plotting the trends
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.plot(merged_data['Date'], merged_data['Transaction Value (AED)'], label='Transaction Value (AED)')
plt.title('Real Estate Transactions Over Time')
plt.xlabel('Date')
plt.ylabel('Transaction Value (AED)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(merged_data['Date'], merged_data['Daily Ridership'], label='Daily Ridership', color='orange')
plt.title('Public Transport Ridership Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Ridership')
plt.legend()

plt.tight_layout()
plt.show()
