#S
n=7
for i in range(1,n+1): 
    for j in range(1,n+1): 
        if(i==1 and 1<j<=n//2+1) or (j==1 and 1<i<=n//2) or (i==n and 1<j<=n//2+1) or (j==n//2+2 and n//2+1<i<n) or (i==n//2+1 and 1<j<=n//2+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
