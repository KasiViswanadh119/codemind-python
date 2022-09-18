a=int(input())
sum=0
for i in range(1,a+1):
    if a%i==0:
        if a==i:
            break
        sum=sum+i
if sum==a:
    print('True')
else:
    print('False')