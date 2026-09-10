n=int(input())
lst=[]
for i in range (n):
    command=input().split()
    if command=="insert":
        lst.insert(int(command[1]),int(command[2]))
    elif command=="print":
        print(lst)
    elif command=="remove":
        lst.remove(int(command[1]))
    elif command=="reverse":
        lst.reverse()
    elif command=="pop":
        lst.pop()


