a=int(input())
sum=0
for i in range(1,a+1):
    if a%i==0:
        if i==a:
            break
        sum=sum+i
if a==sum:
    print(True)
else:
    print(False)