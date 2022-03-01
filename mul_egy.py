
def mul_egy():
    a = int(input("a = "))
    b = int(input("b = "))
    resultat = 0
    while(b > 0):
        if(b % 2 == 0):
            a *= 2
            b /= 2
        else:
            resultat += a
            b -= 1


    print(resultat)

mul_egy();