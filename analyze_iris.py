import pandas as pd
iris = pd.read_csv('data/iris.csv')

print(iris.columns)
print(iris.sample(10).sort_index())
