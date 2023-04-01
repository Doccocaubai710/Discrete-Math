def printSolution():
    global count
    count+=1
    for i in range(1,m+1):
        print(a[i],end=' ')
    print()
def Try(k):
    for j in range(a[k-1]+1,k+n-m+1):
        a[k]=j
        if k==m:
            printSolution()
        else:
            Try(k+1)
if __name__=='__main__':
    n=int(input())
    m=int(input())
    a=[0]*(n+1)
    count=0
    Try(1)
    print(count)