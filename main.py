import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv("software_assets_dataset.csv")

# Show first 5 rows
print(df.head())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Expired software
print("\nExpired Software:")
expired = df[df['Expiry_Date'] < '2026-01-01']
print(expired)

# Save expired software report
expired.to_csv("expired_software_report.csv", index=False)

print("\nReport saved successfully!")

# Department-wise expired software count
print("\nExpired Software by Department:")
print(expired['Department'].value_counts())

# Plot department-wise expired software

expired['Department'].value_counts().plot(kind='bar')

plt.title("Expired Software by Department")
plt.xlabel("Department")
plt.ylabel("Count")

plt.show()