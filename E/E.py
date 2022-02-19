#E
n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1) or (i==1 or i==n) or (i==n//2+1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print('')
