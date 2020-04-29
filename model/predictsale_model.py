import numpy as np
import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression



dataset=pd.read_csv('../data/predictsale.csv')

X=dataset.iloc[:,:3]
y=dataset.iloc[:,-1]

regressor=LinearRegression()
regressor.fit(X,y)

pickle.dump(regressor,open('predictsale_model.pkl','wb'))
model=pickle.load(open('predictsale_model.pkl','rb'))

print(model.predict([[4,300,500]]))
