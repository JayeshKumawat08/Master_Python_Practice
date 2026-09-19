import numpy as np

salaries = np.array([45000,52000,120000,48000,55000])

sal_mean = salaries.mean()
sal_std = salaries.std()

scaled_salaries = (salaries - sal_mean) / sal_std

print("Standardized Salaries")
print(scaled_salaries)