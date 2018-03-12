#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import csv

inputfile = '../data/input.xlsx'
data = pd.read_excel(inputfile) #导入数据

x = data.iloc[:,1:11].as_matrix()
y = data.iloc[:,0].as_matrix()

print x[0:2]
print '**********************************'
print y

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(x,y)
# print model.intercept_
# print model.coef_
print model.score(x,y)
print model.feature_importances_
print '***********************************'
out = model.predict(x)
#把计算结果写入excel
df = pd.DataFrame(out)
df.to_excel('../data/out.xlsx')

fig, ax = plt.subplots()
ax.scatter(y, out)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
