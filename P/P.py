#P
n=7
for i in range(1,n+1): 
    for j in range(1,n+1): 
        if((j==1 ) or (1<j<=n//2 and i==1) or (1<j<=n//2 and i==n//2+1) or (j==n//2+1 and 1<i<=n//2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
