import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
 
# Driver Code
s = {1, 2, 3,4,5,6,7,8,9}
n =9
 
print(findsubsets(s, n))


