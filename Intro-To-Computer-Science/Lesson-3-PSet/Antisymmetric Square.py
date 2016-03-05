# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    n = len(A)
    for e in A:
        if n == len(A[0]):
            i = 0
            while i < n:
                j = 0
                while j < n:
                    if i != j:
                        if A[i][j] == -A[j][i]:
                            j = j+1
                        else:
                            return False
                    else:
                        j = j+1
                i = i+1
            result = True
        else:
            return False
    return result
    #Write your code here


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
