def printSolution():
    global count
    count+=1
    for j in range(1,n+1):
        print(a[j],end=' ')
    print()
def candidate(j,k):
    for i in range(1,k):
        if j==a[i]:
            return 0
    return 1
def Try(k):
    for j in range(1,n+1):
        if candidate(j,k)==1:
            a[k]=j
            if k==n:
                printSolution()
            else:
                Try(k+1)
if __name__=='__main__':
    n=int(input())
    a=[0]*(n+1)
    count=0
    Try(1)
    print(count)

        