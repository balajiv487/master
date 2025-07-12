import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
path = "C:\\Users\\balaj\\Downloads\\homeprices.csv"
df=pd.read_csv(path)
print(df)
plt.xlabel('Area(Sqr Ft)')
plt.ylabel('Price(US $)')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.show()
reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
print(reg.predict([[2600]]))
print(f"Coeeficinet {reg.coef_}")