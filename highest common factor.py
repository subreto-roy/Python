def HCF(a,b):
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if a % i == 0 and b % i == 0:
           ans = i

    return ans


print(HCF(17,30))
