for k in range(int(input())):
    x=int(input())
    y=x
    z=x
    while True:
        is_prime=True
        for i in range(2,int(y**0.5)+1):
            if y%i==0:
                is_prime=False
        if is_prime==True:
            break
        else:
            y=y+1
    #print(y)
    while True:
        is_prime=True
        for c in range(2,int(z**0.5)+1):
            if z%c==0:
                is_prime=False
        if is_prime==True:
            break
        else:
            z=z-1
    #print(z)
    if y-x>x-z:
        print(z)
    elif y-x==x-z:
        print(z)
    else:
        print(y)
           