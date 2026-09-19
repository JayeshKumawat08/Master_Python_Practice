import numpy as np
import matplotlib.pyplot as plt

salaries = np.array([45000,52000,120000,48000,55000])

sal_mean = salaries.mean()
sal_std = salaries.std()

scaled_salaries = (salaries - sal_mean) / sal_std

print("Standardized Salaries")
print(scaled_salaries)

fig, (ax1,ax2) = plt.subplots(1,2, figsize =(10,4))

ax1.plot(salaries, marker='o', color="red", linestyle = 'dashed')
ax1.set_title("Raw Salaries (Notice the massive spike)")
ax1.set_ylabel("Salaries in Rupees")

ax2.plot(scaled_salaries, marker ='o',color='green', linestyle = 'dashed')
ax2.set_title("Standardized Salaries (Z-Scores)")
ax2.set_ylabel("Standard Deviations")
ax2.axhline(0, color ='black', linewidth=1)

plt.tight_layout()
plt.show()
