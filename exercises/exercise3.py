import pandas as pd
import sqlalchemy as sq
df = pd.read_csv("https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv",sep=';',encoding = "iso-8859-15")

df = df.drop([df.index[0],df.index[1],df.index[2],df.index[3],df.index[4]])
df = df.drop([df.index[df.shape[0]-1],df.index[df.shape[0]-2],df.index[df.shape[0]-3],df.index[df.shape[0]-4]])



df.to_sql("cars",'sqlite:///cars.sqlite',if_exists="replace")