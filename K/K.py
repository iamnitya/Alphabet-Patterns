#K
n=9
for i in range(1,n+1): 
    for j in range(1,n+1): 
        if(j==1 or ((i==j+n//2)) or (j==(n-n//2+1-i))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
