import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

class Lib_Analytics:
    def __init__(self):
        self.trend_data = {"Month": ["Jan", "Feb", "Mar", "Apr", "May"], 
                           "Books_Borrowed": [120, 200, 150, 300, 250]}

        self.genre_data = pd.DataFrame({
            "Genre": ["Engineering", "Business", "Engineering", "Arts", 
                      "Engineering", "Business", "Business", "Engineering"]
        })

    def plot_borrow(self):
        print("Line Trend")
        plt.figure(figsize=(8,4))
        plt.plot(self.trend_data["Month"], self.trend_data["Books_Borrowed"],
                marker='o',color='blue',linestyle='--')
        plt.title("Library borrowing trend (matplot)")
        plt.xlabel("Month")
        plt.ylabel("Number of Books")
        plt.grid(True)
        plt.show()

    def popularity(self):
        print("statistical bar plot")

        plt.figure(figsize=(8,4))
        sns.countplot(data=self.genre_data, x="Genre", palette="viridis")

        plt.title("Book Genre Popularity (Seaborn)")
        plt.xlabel("Book Category")
        plt.ylabel("Total Borrows")
        plt.show()

if __name__ == "__main__":
    analy = Lib_Analytics()
    analy.plot_borrow()
    analy.popularity()
