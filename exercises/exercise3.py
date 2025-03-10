import pandas as pd
import sqlalchemy as sq

def valint(input):
    if input == "-":
        return False
    return int(input) > 0

def valcin(input):
    if (type(input) != str):
        return False
    if len(input) == 5:
        return True

fields = range(83)
df = pd.read_csv("https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv",dtype=str,header=None,sep=';',encoding = "iso-8859-15",names = fields)

for i in range(1,8):
    df = df.drop(df.index[0])
df = df.drop([df.index[df.shape[0]-1],df.index[df.shape[0]-2],df.index[df.shape[0]-3],df.index[df.shape[0]-4]])

df.drop(df.iloc[:, 3:12], inplace=True, axis=1)
df.drop(df.iloc[:, 4:13], inplace=True, axis=1)
df.drop(df.iloc[:, 5:14], inplace=True, axis=1)
df.drop(df.iloc[:, 6:15], inplace=True, axis=1)
df.drop(df.iloc[:, 7:16], inplace=True, axis=1)
df.drop(df.iloc[:, 8:17], inplace=True, axis=1)
df.drop(df.iloc[:, 9:18], inplace=True, axis=1)
df.drop(df.iloc[:, 10:20], inplace=True, axis=1)
#df.rename({'0': 'date', '1': 'CIN','2': 'name', '12': 'petrol','22': 'diesel', '32': 'gas','42': 'electro', '52': 'hybrid','62': 'plugInHybrid', '72': 'others'},axis = 1, inplace=True)
df = df.set_axis(['date', 'CIN','name',  'petrol', 'diesel',  'gas', 'electro',  'hybrid', 'plugInHybrid', 'others'],axis=1)

df = df[df["petrol"].apply(lambda x: valint(x))]

df = df[df["CIN"].apply(lambda x: valcin(x))]

df.to_sql("cars",'sqlite:///cars.sqlite',if_exists="replace",index = False, dtype={
    "date": sq.TEXT,
    "name": sq.TEXT,
    "CIN": sq.TEXT,
    'petrol': sq.BIGINT,
    'diesel': sq.BIGINT, 
    'gas': sq.BIGINT,
    'electro': sq.BIGINT, 
    'hybrid': sq.BIGINT,
    'plugInHybrid': sq.BIGINT,
    'others': sq.BIGINT
})