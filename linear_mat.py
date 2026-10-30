import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyst:
    def __init__(self):
        sns.set_theme(style="whitegrid", palette = "muted")

        normal_users = np.random.normal(30,10,200)
        bots = np.array([500]*10)

        self.raw_time = np.concatenate([normal_users,bots])
        self.cleaned_time = np.where(self.raw_time > 120, 120, self.raw_time)

    def plot_preprocessing_impact(self):
        print("\t\t\tDensity Plot\n")
        plt.figure(figsize=(10,6))

        sns.kdeplot(self.raw_time, fill=True, color='red', alpha=0.4, label= "Raw Data (with bot outliers)")

        sns.kdeplot(self.cleaned_time, fill=True, color='blue', alpha=0.7, label="Cleaned Data")

        plt.title("Impact of Preprocessing on User Session Time", fontsize= 14, fontwidth ='bold', pad=15)
        plt.xlabel("Time Spent on Site",fontsize=12,fontwidth='bold')
        plt.ylabel("Density (Frequency)",fontsize = 12, fontwidth='bold')

        plt.xlim(0,150)
        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    analyst = DataAnalyst()
    analyst.plot_preprocessing_impact
