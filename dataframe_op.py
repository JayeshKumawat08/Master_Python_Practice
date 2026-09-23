import pandas as pd

data = {
    "Acc_No": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikram"],
    "Balance": [50000, 120000, 45000, 85000, 200000]
}
df = pd.DataFrame(data)
print(df)
print()
#interger location iloc
first = df.iloc[0]
print(first)
print()

first_three = df.iloc[0:3,:]
print(first_three)

print('-'*50)

#label location loc
name_money = df.loc[:,['Name','Balance']]
print(name_money)
print()

rich = df.loc[df['Balance']>60000,:]
print(rich)

