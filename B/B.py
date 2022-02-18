n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1) or (i==n and j!=n) or ((i==1 or i==n//2+1 or i==n) and j!=n) or (i!=n and i!=1 and i!=n//2+1 and j==n):
            print('*', end=' ')
        else:
            print(" ", end=' ')
    print('')    
