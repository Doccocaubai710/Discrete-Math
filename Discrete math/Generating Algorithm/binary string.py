#Generate binary string of length n: from a[0] to a[n-1]
#Solving by run from right to left, if we catch a 0, then turn it to 1 and make the remaining become 0 again
def printarray(arr,n):
    for i in range(n):
        print(arr[i],end=' ')
    print()
def generateAllBinaryString(n,arr,i):
    if i==n:
        printarray(arr,n)
        return 
    # First assign "0" at ith position and try for all other permutations for remaining positions
    arr[i] = 0
    generateAllBinaryString(n, arr, i + 1)
 
    # And then assign "1" at ith position and try for all other permutations for remaining positions
    arr[i] = 1
    generateAllBinaryString(n, arr, i + 1)        
if __name__ == "__main__":
 
    n = 4
    arr = [None] * n
 
    # Print all binary strings
    generateAllBinaryString(n, arr, 0)