import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

"""
print(sns.get_dataset_names())
df=sns.load_dataset("diamonds")
#diss=np.array(df[["x","y","z"]])
#print(np.concatenate((diss,np.array(diss[:,0]*diss[:,1]*diss[:,2]).reshape(53940,1)),axis=1))
xyz=df.loc[:,["x","y","z"]].head(10)
xyz=pd.DataFrame(xyz)
print(list(xyz.x).count(3.95))

print(df.cut.value_counts().index)
print(df.cut.value_counts().values)
print(df.value_counts())
sns.set()
sns.barplot(df.cut.value_counts().index,df.cut.value_counts().values,data=df,hue_order="color")
plt.show()
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





