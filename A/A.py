#A
n=7
for i in range(n):
    for j in range(n):
        if((i==n//2 and 0<j<n-1) or (i==0 and 0<j<n-1) or ((j==0 or j==n-1) and i!=0)):
            print('*', end=' ')
        else:
            print(" ", end=' ')
    print('')
