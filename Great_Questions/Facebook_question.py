"""

This problem was asked by Facebook.
Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's  -10 * -10 * 5.
You can assume the list has at least three integers.

"""

import numpy as np
trip=[-10, 10,5,2]
stat=np.prod(trip)
if stat>0:print(np.prod(sorted([abs(j) for j in trip],reverse=True)[:3]))
else:print(np.prod(sorted(trip,reverse=True)[:3]))

"""
import pandas as pd
import itertools
df=pd.DataFrame(itertools.permutations([-10,-10,5,2], 3))
s=df[0]*df[1]*df[2]
print(s.max())
"""
#print(len(list(itertools.permutations([4,5,8,9],3))))