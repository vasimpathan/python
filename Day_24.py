import matplotlib.pyplot as plt
# Hours vs Marks
# Hours: 2, 4, 6, 8, 10
# Marks: 21, 38, 64, 85, 98

hours = [2, 4, 6, 8, 10]
math_marks = [21, 38, 64, 85, 98]
sci_marks = [10, 15, 19, 25, 35]

plt.scatter(hours, math_marks, label = "math")
plt.scatter(hours, sci_marks, label = "sci")
plt.xlabel("Hours spent")
plt.ylabel("Marks scored")
plt.title("Students data of hours spent vs marks scored")
plt.legend()
plt.show()