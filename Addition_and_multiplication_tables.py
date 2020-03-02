def galois(n):
    mul = [[format(i*j, '0{}b'.format(n)) for i in range(n)] for j in range(n)]
    add = [[format(i+j, '0{}b'.format(n)) for i in range(n)] for j in range(n)]
    return mul, add

##    Optional code for printing the tables
##
##    print("Addition Table")
##    for i in range(n):
##        for j in range(n):
##            print(add[i][j], end = " ")
##        print()
##
##    print("\nMultiplication Table")
##    for i in range(n):
##        for j in range(n):
##            print(mul[i][j], end = " ")
##        print()
