from matplotlib import pyplot as plt
plt.style.use("ggplot")

age_x = [25,26,27,28,29,30,31,32,33,34,35]

#Median Developer salaries by age
dev_y = [38465,42000,46752,49802,53000,76590,56000,78000,67548,58909,75448]

#Median Python Developer Salaries by age
py_dev_y = [45678,56744,31332,70004,75467,21789,56789,23782,45678,78449,83442]

#Median Javascript Developer Salaries by age
js_dev_y = [37810,42156,46781,49879,53782,70003,56789,34456,78887,67895,43890]

plt.plot(age_x,dev_y, color="k", linestyle="--", marker="o", label="All Developers")
plt.plot(age_x,py_dev_y, color="b", marker="o", linewidth=3, label="Python Developers")
plt.plot(age_x,js_dev_y, color="y", marker="o", linewidth=3,label="JavaScript Developers")

plt.xlabel("Age")
plt.ylabel("Pay - USD")
plt.title("Median Salary For Different Developers")
plt.grid(True)
plt.legend()
plt.show()
