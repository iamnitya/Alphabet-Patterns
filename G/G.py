#G
n=7
for i in range(n): 
    for j in range(n): 
        if ((i == 0 and (j != 0 and j != n-1)) or               
                (i == n - 1 and (j != 0 and j != n-1)) or                
                ((j == 0 and (i != 0 and i != n-1)) or                 
                 (j == n-1 and i != n-1 and i >= (n/2)-1)) or                
                (i == (n/2)-1 and ((n/2)-1 <= col < n-1)) or (i==n//2 and j>n//2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
