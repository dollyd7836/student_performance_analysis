import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students.csv")

print("\n===== STUDENT ANALYSIS REPORT =====\n")

# Add Result column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Show full data
print(df)

# Pass & Fail
pass_students = df[df["Result"] == "Pass"]
fail_students = df[df["Result"] == "Fail"]

print("\nPass Students:\n", pass_students)
print("\nFail Students:\n", fail_students)

# Stats
print("\nAverage:", df["Marks"].mean())
print("Max:", df["Marks"].max())
print("Min:", df["Marks"].min())

# City analysis
city_avg = df.groupby("City")["Marks"].mean()
print("\nCity Avg:\n", city_avg)

# Topper
topper = df.loc[df["Marks"].idxmax()]
print("\nTopper:\n", topper)

# Graph
city_avg.plot(kind="bar")
plt.show()