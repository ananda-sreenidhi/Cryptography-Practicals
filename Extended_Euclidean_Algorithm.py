def euclidean_gcd(r1, r2): 
    n = max(r1, r2) #The greater number of the two is usually the modulo part
    r1, r2 = max(r1, r2), min(r1, r2)
    s1, s2, t1, t2 = 1, 0, 0, 1 #Initialising s, t values for the Extended Euclidean Algorithm
    while r2 != 0: 
        q, r = r1//r2, r1%r2 
        s, t = s1-q*s2, t1-q*t2 
        r1, r2, s1, s2, t1, t2 = r2, r, s2, s, t2, t #Swapping as per the algorithm
    gcd = r1
    if gcd != 1: 
        return None 
    else: 
        return t1 % n #Taking care of values greater than n and negative values
