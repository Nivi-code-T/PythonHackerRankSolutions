student={ }
n=int(input())
for i in range(n):
    data=input().split()
    name=data[0]
    marks=list(map(float,data[1:]))
    student[name]=marks
query_name=input()
marks=student[query_name]
average=(marks[0]+marks[1]+marks[2])/3
print("%.2f" % average)
