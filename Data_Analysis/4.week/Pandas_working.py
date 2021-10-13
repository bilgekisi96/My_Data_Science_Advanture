import pandas as pd
import numpy as np
df=pd.read_csv("titanic_train.csv")
print(df.head(-15))
print(df.describe())
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.dtypes)
print(df.sort_values(by="Fare"))
print(df.Fare.value_counts())

dates=pd.date_range("01/01/2021",periods=8)
df=pd.DataFrame(np.random.randn(8,4),index=list("abcdefgh"),columns=["A","B","C","D"])
#print(df.value_counts())
#print(df.sort_values("B"))
print(df.loc["b"]>0)
print(df.loc["b":"g","C"])
print(df.loc[lambda df:df["C"]>0,:])

