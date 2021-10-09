import numpy as np
import seaborn as sns

print(sns.get_dataset_names())
df=sns.load_dataset("diamonds")
diss=np.array(df[["x","y","z"]])
print(np.concatenate((diss,np.array(diss[:,0]*diss[:,1]*diss[:,2]).reshape(53940,1)),axis=1))

