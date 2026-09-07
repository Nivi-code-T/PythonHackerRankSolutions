students=[]
n=int(input())
for i in range(n):
    name=input()
    grades=float(input())
    students.append([name,grades])
print(students)

grades=[]
for student in students:
    grades.append(student[1])
print(grades)
grades=sorted(set(grades))
second_lowest=grades[1]
print(second_lowest)

names=[]
for student in students:
    if student[1]==second_lowest:
        names.append(student[0])
names.sort()
print(names)

for name in names:
    print(name)