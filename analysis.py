import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

print("\nFULL DATA")
print(df)

# Pass / Fail students
pass_students = df[df["Marks"] >= 50]
fail_students = df[df["Marks"] < 50]

print("\nPASS STUDENTS")
print(pass_students)

print("\nFAIL STUDENTS")
print(fail_students)

# Basic statistics
print("\nAVERAGE MARKS (PASS):", pass_students["Marks"].mean())
print("AVERAGE MARKS (FAIL):", fail_students["Marks"].mean())
print("HIGHEST MARK:", df["Marks"].max())
print("LOWEST MARK:", df["Marks"].min())

# City-wise analysis
city_avg = df.groupby("City")["Marks"].mean()
city_count = df.groupby("City")["Name"].count()

print("\nCITY-WISE AVERAGE MARKS")
print(city_avg)

print("\nCITY-WISE STUDENT COUNT")
print(city_count)

# Insights
top_city = city_avg.idxmax()
top_student = df.loc[df["Marks"].idxmax(), "Name"]

print("\nTOP PERFORMING CITY:", top_city)
print("TOP STUDENT:", top_student)

# Save outputs
pass_students.to_csv("pass_students.csv", index=False)
fail_students.to_csv("fail_students.csv", index=False)
city_avg.to_csv("city_avg_marks.csv")

print("\nFILES SAVED SUCCESSFULLY!")

# Visualization
city_avg.plot(kind="bar")
plt.title("City-wise Average Marks")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()