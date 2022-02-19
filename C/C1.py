n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1 and i!=1 and i!=n) or (i==1 and j>1 and j<n) or (i==n and j>1 and j<n):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print('')
