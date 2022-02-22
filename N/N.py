#N
n=7
for i in range(1,n+1): 
    for j in range(1,n+1): 
        if((j==1 or j==n) or (j==n//2+1 and i==n//2+1) or (i==j)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
