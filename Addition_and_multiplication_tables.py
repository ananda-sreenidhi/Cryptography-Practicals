def galois(n):
    #creates a 2x2 list mul and fills it with product of row and column
    mul = [[format(i*j, '0{}b'.format(n)) for i in range(n)] for j in range(n)] 
    #creates a 2x2 list add and fills it with sum of row and column
    add = [[format(i+j, '0{}b'.format(n)) for i in range(n)] for j in range(n)]
    return mul, add

##    Optional code for printing the tables
##
##    print("Addition Table")
##    for i in range(n):
##        for j in range(n):
##            print(add[i][j], end = "\t")
##        print()
##
##    print("\nMultiplication Table")
##    for i in range(n):
##        for j in range(n):
##            print(mul[i][j], end = "\t")
##        print()
