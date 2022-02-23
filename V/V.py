#O
n=7
for i in range(1,n+1): 
    for j in range(1,2*n): 
        if(i==j) or (i==2*n-j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
