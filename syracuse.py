def syracuse(n):
    while n !=1:
        print(n, end = ',')
        if (n%2==1):
            n = n*3+1
        else:
            n=n/2

syracuse(5)