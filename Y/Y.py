#Y
n=7
for i in range(1,n+1): 
    for j in range(1,n+1): 
        if((j==n//2+1 and i==n//2+1) or (i==j and i<=n//2+1) or ((j==(n+1-i) and i<=n//2+1)) or i>n//2+1 and j==n//2+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
