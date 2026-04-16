import matplotlib.pyplot as plt

cities = ["Delhi", "Mumbai"]
marks = [80, 60]

plt.bar(cities, marks)

plt.title("City vs Marks")
plt.xlabel("Cities")
plt.ylabel("Marks")

plt.show()