import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data={
    "exp" : [1,2,3,4,5],
    "salary":[20000,30000,40000,50000,60000]
}

df=pd.DataFrame(data)
x=df[["exp"]]
y=df['salary']

model=LinearRegression()

model.fit(x,y)

pickle.dump(model,open('model.pkl','wb'))

print("model trained & saved")