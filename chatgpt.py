'''age = input("enter your age= ")
age = int(age)
print(type(age))'''
'''num1=int(input("enter first no="))
num2=int(input("enter second no="))
print("sum is=",num1+num2)'''
'''name=input("enter your name=")
age=int(input("enter your age="))
print("hello",name,"you are 17")'''
'''age=int(input("enter your age="))
if(age>=18):
 print("you are an adult!")
else:
 print("you are minor!")'''
'''rain=input("enter rain=")
if("rain is",rain):
    print("take umbrella!")
else:
    print("dont take!")'''
'''rain = False
if rain:
    print("Umbrella lo!")
else:
    print("Umbrella mat lo!")'''
'''=int(input("enter a no"))
if(num>0):
    print("positive")
elif(num<0):
    print("negative")
else:
    print("zero")'''
"""le True:
    name = input("Enter any name (type quit to stop): ")
    if name == "quit":
        break
    print("Hello", name)"""
""" greet(name):
    print("Hello",name)
    print("How are you?")
greet("dolly")
greet("tripti")
greet("khushi")"""

'''1=int(input("enter 1st no"))
num2=int(input("enter 2nd no"))
add=num1+num2
print("result is=",add)'''
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add(a,b):
    result=a+b
    return result
answer=add(a,b)
print("sum is",answer)'''
'''e=input("enter your name")
age=int(input("enter your age"))
if(age>=18):
    print("welcome!")
else:

    print("sorry!")'''
'''name=input("enter your name")
age=int(input("enter your age"))
def vote(name,age):
  if(age>=18):
    print("hey",name,"you can vote!")
  else:
    print("hey",name,"you cant vote!")
vote(name,age)'''
'''ds=["momo","burger","golgappa","tikki","sandwich"]
print(foods)
print(foods[0])'''
"""ds=["momo","burger","golgappa","tikki","sandwich"]
foods.append("pizza")
print(foods)"""
'''ds=["momo","burger","golgappa","tikki","sandwich"]
print(len(foods))'''


'''ends=["khushi","raksha","dolly","tripti"]
for friend in friends:
    print("hello",friend)'''
''''
student={"name":"dolly","age":19,"college":"ngf"}
student["city"]="palwal"
student["age"]=20
del student["college"]
print(student)'''
''''
student = {
    "name": "Dolly",
    "age": 19,
    "city": "Palwal",
    "hoby":"watching cricket"
}

for key, value in student.items():
    print(key, ":", value)'''
''''
name="dolly dhingra"
print(name.upper())
print(name.lower())
print(name.title())
print(len(name))
print(name.replace("dolly","tripti"))
'''
''''
name = "Dolly Dhingra"


print(name.strip())        # spaces hatao
print(name.startswith("D")) # D se shuru?
print(name.endswith("a"))   # a pe khatam?
print("Dolly" in name)      # "Dolly" hai andar?'''
name=input("enter a name")
print(name.upper())
print(len(name))
print("python" in name)






'''name="dolly"
age=19
subject1="maths"
subject2="eng"
subject3="daa"
marks=[32,67,89]
passed=True
print(name)
print(age)
print(subject1,subject2,subject3)
print(marks)
print(passed)'''
'''marks=[40,55,70]
for m in marks:
    if m>=50:
        print("pass:",m)
    else:
        print("fail",m)'''
'''students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 40},
    {"name": "C", "marks": 70}
]
for student in students:
    if student["marks"]>=50:
        print(student["name"])'''
        
'''students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 40},
    {"name": "C", "marks": 70}
]
total=0
for student in students:
    total=total+student["marks"
                        ]
average=total/len(students)
print("total=",total)
print("average=",average)'''
'''students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 40},
    {"name": "C", "marks": 70}
]
highest=0
top_student=""
for student in students:
    if student["marks"]>highest:
        highest=student["marks"]
        top_student=student["name"]
        print("top student=",top_student)'''
'''nums = [10, 25, 5, 40, 30]
max=0
for n in nums:
    if n>max:
        max=n
print("max=",max)'''
'''nums = [5, 2, 8, 1]
min=nums[0]
for n in nums:
    if n<min:
        min=n
print("min=",min)   ''' 
'''nums = [10, 20, 30, 40]
total=0
for n in nums:
    total=total+ n 
    average=total/len(nums)
print("total =",total)   
print("average=",average)'''
'''
nums = [10,20,30,40]
total=0
max_num=0
for n in nums:
    total=total+n
    if n>max_num:
        max_num=n
average=total/len(nums)
print("total=",total)
print("avg=",average)
print("max=",max_num)'''
'''nums = [2, 4, 6, 8]
for n in nums:
    if n%2==0:
        print("even",n)
    else:
        print("odd",n)'''
'''def print_name(name):
    print(name)
    print_name("dolly")'''
'''def square(n):
    print(n**2)
square(5)    '''
'''def multiply(a,b):
    return a*b
result=multiply(3,5)
print(result)'''
'''students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 40},
    {"name": "C", "marks": 70}
]

total=0
average=0
pass_count=0
fail_count=0
for student in students:
      total=total+student["marks"]
      if student["marks"]>=50:
            pass_count+=1
      else:
            fail_count+=1

      average=total/len(students)
print("total:",total)
print("average:",average)
print("passed",pass_count)
print("failed",fail_count)'''
'''nums = [10, 25, 60, 45, 80]

total = 0
count = 0

for n in nums:
    total = total+n

    if n > 50:
        count = count+1

print("total =", total)
print("count =", count)'''
'''nums = [10, 25, 60, 45, 80]
max_num=0
min_num=nums[0]
for n in nums:
    if n>max_num:
     max_num=n
    else:
     min_num=n
print("max no is=",max_num)
print("min no is=",min_num)     '''
'''import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "marks": [80, 40, 70]
}
df=pd.DataFrame(data)
print(df)'''
'''import pandas as pd
data={
    "Name" :["a","b","c"],"Marks": [10, 60, 30]}
df=pd.DataFrame(data)
print(df["Marks"].sum())
print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())'''
'''nums = [2, 5, 8, 1, 10]
for n in nums:
    if n%2==0:
        print("even",n)
    else:
        print("odd",n)'''
'''ort pandas as pd

data = {
    "Marks": [10, 50, 80, 30]
}

df = pd.DataFrame(data)
print(df[(df["Marks"]<50)|(df["Marks"]==80)])'''
'''
import pandas as pd

data = {
    "Marks": [25, 60, 90, 45, 80]
}

df = pd.DataFrame(data)
print(df[(df["Marks"]>40)|(df["Marks"]!=90)])'''
'''import pandas as pd
df=pd.read_csv("students.csv")
pass_students=df[df["Marks"]>=50]
print(pass_students)
print(pass_students["Marks"].max())'''
'''import pandas as pd
df=pd.read_csv("students.csv")
print(len(df))
pass_students=df[df["Marks"]>=50]
print(pass_students)
fail_students=df[df["Marks"]<50]
print(fail_students)
print(pass_students["Marks"].mean())
print(fail_students["Marks"].mean())'''
'''import pandas as pd
df=pd.read_csv("students2.csv")
Delhi=df[df["City"]=="Delhi"]
print(Delhi)
passed_Delhi=Delhi[Delhi["Marks"]>=50]
print(passed_Delhi)'''
'''import pandas as pd
df=pd.read_csv("students2.csv")
print(df[(df["City"]=="Mumbai")|(df["City"]=="Noida")])
'''
'''import pandas as pd
df=pd.read_csv("students2.csv")
Delhi_students=df[df["City"]=="Delhi"]
print(Delhi_students)
print(Delhi_students["Marks"].mean())'''
"""import pandas as pd
df=pd.read_csv("students2.csv")
print(df.groupby("City")["Name"].count())"""


"""
import pandas as pd
df=pd.read_csv("students_project.csv")
print(df)
print(len(df))
passed_students=df[df["Marks"]>=50]
print(passed_students)
print(passed_students["Marks"].mean())
failed_students=df[df["Marks"]<50]
print(failed_students)
print(failed_students["Marks"].mean())"""
"""import pandas as pd
df=pd.read_csv("students2.csv")
city_total=df.groupby("City")["Name"].count()
print(city_total)
city_avg=df.groupby("City")["Marks"].mean()
print(city_avg)
pass_city = df[df["Marks"]>=50].groupby("City")["Name"].count()
fail_city = df[df["Marks"]<50].groupby("City")["Name"].count()

print("Pass per city:\n", pass_city)
print("Fail per city:\n", fail_city)"""

"""import pandas as pd

df = pd.read_csv("students_project.csv")

# Total students per city
city_total = df.groupby("City")["Name"].count()
print("Total students per city:\n", city_total)
print("-"*30)

# Pass students per city
pass_city = df[df["Marks"] >= 50].groupby("City")["Name"].count()
print("Pass students per city:\n", pass_city)
print("-"*30)

# Fail students per city
fail_city = df[df["Marks"] < 50].groupby("City")["Name"].count()
print("Fail students per city:\n", fail_city)
print("-"*30)

# Average marks per city
city_avg = df.groupby("City")["Marks"].mean()
print("Average marks per city:\n", city_avg)
print("-"*30)"""
""""
import pandas as pd
data=({"Subject":["Maths","Science","Evs","Hindi","Sst"],"Marks":[89,67,79,45,38]})
df=pd.DataFrame(data)
passed_students=df[df["Marks"]>=50]
print("pass students:",passed_students)
print((passed_students["Marks"].mean()))
failed_students=df[df["Marks"]<50]
print("fail students:",failed_students)
print(failed_students["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())"""
""""
#main code
import pandas as pd

# Data
data = {
    "Subject": ["Maths", "Science", "Evs", "Hindi", "Sst"],
    "Marks": [89, 67, 79, 45, 38]
}

# DataFrame
df = pd.DataFrame(data)

# Pass students
passed_students = df[df["Marks"] >= 50]
print("Pass students:\n", passed_students)

# Fail students
failed_students = df[df["Marks"] < 50]
print("\nFail students:\n", failed_students)

# Average marks
print("\nAverage Marks (Pass):", passed_students["Marks"].mean())
print("Average Marks (Fail):", failed_students["Marks"].mean())

# Max & Min
print("\nMax Marks:", df["Marks"].max())
print("Min Marks:", df["Marks"].min())

# Add Result column (one-line smart way)
df["Result"] = ["Pass" if m >= 50 else "Fail" for m in df["Marks"]]

print("\nFull Data with Result:\n", df)

# Show only Fail students using Result column
print("\nOnly Fail students:\n", df[df["Result"] == "Fail"])

# Count Pass & Fail
print("\nCount of Pass/Fail:\n", df["Result"].value_counts())"""
marks = [80, 40, 70, 30, 90]
print(max(marks))