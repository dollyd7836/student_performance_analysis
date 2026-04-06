import pandas as pd

# Read data
df = pd.read_csv("students.csv")

# Show data
print("Full Data:\n", df)
print("-"*30)

# Pass students
pass_students = df[df["Marks"] >= 50]
print("Pass students:\n", pass_students)
print("-"*30)

# Fail students
fail_students = df[df["Marks"] < 50]
print("Fail students:\n", fail_students)
print("-"*30)

# Average marks
print("Average Marks (Pass):", pass_students["Marks"].mean())
print("Average Marks (Fail):", fail_students["Marks"].mean())
print("-"*30)

# City-wise average
print("City-wise Average:\n", df.groupby("City")["Marks"].mean())
print("-"*30)

# City-wise student count
print("Students per City:\n", df.groupby("City")["Name"].count())