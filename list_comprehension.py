def list ():
    result=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    result.append([i,j,k])
    return result

x=int(input())
y=int(input())
z=int(input())
n=int(input())
print(list())