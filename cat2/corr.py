import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Marketing_Spend": [1000, 2000, 3000, 4000, 5000],
    "Website_Visits": [500, 600, 550, 800, 750],
    "Total_Sales": [15000, 25000, 35000, 45000, 55000],
    "Product_Price": [100, 100, 100, 100, 100]
}
df = pd.DataFrame(data)

# 1. Calculate the mathematical correlation matrix
correlation_matrix = df.corr()

# Display the raw matrix in the console
print("--- Correlation Matrix ---")
print(correlation_matrix)

# 2. Visually plot the heatmap
plt.figure(figsize=(8, 6))
# annot=True forces Seaborn to print the exact decimal values inside the colored boxes
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("E-Commerce Feature Correlation")
plt.show()