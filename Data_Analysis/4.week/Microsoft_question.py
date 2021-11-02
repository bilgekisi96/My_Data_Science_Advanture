import numpy as np
"""
This problem was asked by Microsoft.
Given a 2D matrix of characters and a target word, write a function 
that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, 
since it's the leftmost column. Similarly, 
given the target word 'MASS', you should return true, since it's the last row.
"""

def deplt(word):
    mat=np.array([['F', 'A', 'C', 'I'],
                  ['O', 'B', 'Q', 'P'],
                  ['A', 'N', 'O', 'B'],
                  ['M', 'A', 'S', 'S']])
    up_down=["".join(mat[:,i]) for i in range(len(mat))]
    left_right=["".join(mat[j]) for j in range(len(mat))]
    if (word in up_down) or (word in left_right):return True
    else:return False
print(deplt("FOAM"))
print(deplt("MASS"))