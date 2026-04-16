import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_csv("students.csv")

print("\n================ FULL DATA ================\n")
print(df)

# -----------------------
# PASS / FAIL ANALYSIS
# -----------------------
pass_students = df[df["Marks"] >= 50]
fail_students = df[df["Marks"] < 50]

print("\n================ PASS STUDENTS ================\n")
print(pass_students)

print("\n================ FAIL STUDENTS ================\n")
print(fail_students)

# -----------------------
# BASIC STATS
# -----------------------
print("\nAverage Marks (Pass):", pass_students["Marks"].mean())
print("Average Marks (Fail):", fail_students["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# -----------------------
# CITY ANALYSIS
# -----------------------
city_avg = df.groupby("City")["Marks"].mean()
city_count = df.groupby("City")["Name"].count()

print("\n================ CITY WISE AVERAGE ================\n")
print(city_avg)

print("\n================ CITY WISE STUDENT COUNT ================\n")
print(city_count)

# -----------------------
# INSIGHT (IMPORTANT PART)
# -----------------------
top_city = city_avg.idxmax()
best_student = df.loc[df["Marks"].idxmax(), "Name"]

print("\n================ INSIGHTS ================\n")
print("Top Performing City:", top_city)
print("Top Student:", best_student)

# -----------------------
# SAVE FILES
# -----------------------
pass_students.to_csv("pass_students.csv", index=False)
fail_students.to_csv("fail_students.csv", index=False)
city_avg.to_csv("city_avg_marks.csv")

print("\nFiles exported successfully!")

# -----------------------
# VISUALIZATION
# -----------------------
plt.figure(figsize=(6,4))
city_avg.plot(kind="bar", color="skyblue")

plt.title("City-wise Average Marks Analysis")
plt.xlabel("City")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.show()