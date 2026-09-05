import pandas as pd

# Sample Dataset - https://raw.githubusercontent.com/dsrscientist/dataset1/master/titanic_train.csv

# data = {
#     'Name':['Karthick','John','David','Sheik'],
#     'Age':[23,24,25,26],
#     'Marks':[80,90,83,70]
# }

# df=pd.DataFrame(data)

# print(df)

df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/dataset1/master/titanic_train.csv')

print('Shape : ',df.shape)

# print(df.head())
# print(df.tail())
# print(df.info())
df=df.drop(columns=['Cabin'])

# print(df.info())

# print(df['Age'])

avg_age=df['Age'].mean()
df['Age']=df['Age'].fillna(avg_age)

# print('Average age : ',avg_age)
# print(df['Age'].tail())

# print(df.info())
# TODO : duplicate()  dropduplicate()

# indexed location or integer location
# print(df.iloc[5])
# print(df.iloc[6:10])

# cleaned_dataset=df.copy()

# print(df['Age'].describe())