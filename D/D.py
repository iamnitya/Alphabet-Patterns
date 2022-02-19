#D
n=6
for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i!=1 and i!=n) and j==n) or (j==1) or ((i==1 or i==n) and j!=n):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print('')
