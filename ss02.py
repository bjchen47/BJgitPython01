import pandas as pd
ss1=pd.Series([4,7,-5,3],index=['a','b','c','d'])

print(ss1.index)
print(ss1['a'])
print('a' in ss1)
print(7 in ss1)
print(7 in ss1.values)




