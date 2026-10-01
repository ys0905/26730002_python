lst=[]

while True:
    n=int(input())
    if n==0:
        break
    lst.append(n)

    for i in lst:
        if i%2==1:
            print(lst[i])
