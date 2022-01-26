
"""
This problem was asked by Amazon.
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:
"""

import numpy as np
mat=np.array([[1,  2,  3,  4,  5],
              [6,  7,  8,  9,  10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]])
lis,sifir,bos=[j for i in mat for j in i],0,[]
a,b=mat.shape
while True:
    a,b=a-1,b-1
    degisken,dol = list(mat[sifir])+list(mat[:,b])+list(mat[a][::-1])+list(mat[:,sifir][::-1]),[]
    sifir += 1
    for was in degisken:
        if was in bos:pass
        else:bos.append(was)
    if len(bos)==len(lis):break
print(bos)













