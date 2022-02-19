#J
n=7
for i in range(1,n+1): 
    for j in range(1,n+1): 
        if((j==n//2+1 and i!=n or i==1) or ((j<=n//2 and j!=1) and i==n) or (j==1 and i==n-1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
