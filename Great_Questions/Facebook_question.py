"""

This problem was asked by Facebook.
Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's  -10 * -10 * 5.
You can assume the list has at least three integers.

"""

import numpy as np
trip,stat=[-10, -10,5,2],1
for i in trip:stat*=i
if stat>0:print(np.prod(sorted([abs(j) for j in trip],reverse=True)[:3]))
else:print(np.prod(sorted(trip,reverse=True)[:3]))

