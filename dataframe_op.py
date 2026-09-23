import pandas as pd

data = {
    "Acc_No": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikram"],
    "Balance": [50000, 120000, 45000, 85000, 200000]
}
df = pd.DataFrame(data)
print(df)
print()
first = df.iloc[0]
print(first)
print()

first_three = df.iloc[0:3,:]
print(first_three)

print('-'*50)
