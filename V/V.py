#O
n=7
for i in range(1,n+1): 
    for j in range(1,n+1): 
        if(j==1 and 1<=i<=n-1) or (j==n//2+2 and 1<=i<=n-1) or (i==n and 1<j<=n//2+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
