import seaborn as sns
import numpy as np
a = [1,1,1,1,1,2,2,2,2,3,3,1,4,4,5,5,6,7,8,9,11]

print(f"mean:{np.mean(a)}")
print(np.median(a))
print(np.var(a))
print(np.std(a))

print(np.random.rand(5)*10)
print(np.random.rand(5,3))#matris oluşturabiliriz ilk satır sayısı sonrası sütuns sayısı
print(np.random.randint(5,10))

import matplotlib.pyplot as plt
veri=np.random.rand(5,3)
plt.hist(veri)
plt.show()

np.random.rand(5,3)
arrn = np.random.randn(99999)#random normal dağılım
plt.hist(arrn,bins=100)
plt.show()

np.random.rand(5,3)
arr = np.random.randn(9)#random dağılım
plt.hist(arr,bins=100)
plt.show()

print(np.random.randn(3,3))

print(arr.mean(),arr.std())
print(arr.var())
















