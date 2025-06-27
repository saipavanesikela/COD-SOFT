n=int(input("enter the number upto which you want the sum"))
result=[]

for i in range(2,n):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
    if prime:
        result.append(i)

print(sum(result))