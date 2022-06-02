n=int(input())
n1=0
n2=1
sum=0
for i in range(0,n):
    n1=n2
    n2=sum
    sum=n1+n2
    print(n2,end=' ')