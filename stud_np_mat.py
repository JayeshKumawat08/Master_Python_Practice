import numpy as np 
import matplotlib.pyplot as plt

student = np.array(["Jayesh","Sogani","Vivek","Prashant","Uday","Pandu","Charchit","thapa","adi"])

maths = np.array([100,90,87,68,54,49,87,68,89])
phy = np.array([79,56,78,46,98,67,70,83,58])
cs = np.array([90,56,75,86,46,97,67,39,79])

avg_maths = np.mean(maths)
print(f"Avverage Marks of Students in Maths: {avg_maths}")
print('-'*40)

high_phy = np.argmax(phy)
print(f"Highest marks in Physics : {student[high_phy]} Marks: {phy[high_phy]}")

high_cs = np.argmax(cs)
print(f"Highest marks is Computer Science: {student[high_phy]}  Marks: {cs[high_cs]}")

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.bar(student,maths,label="Mathematics")
plt.title("Mathematics Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(student,cs,marker ='o',label = "Computer Science")
plt.title("Computer Science Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid()

plt.suptitle("Academic Performance of Students")

plt.tight_layout()
plt.show()