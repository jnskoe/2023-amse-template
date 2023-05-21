import pandas as pd
import sqlalchemy as sq
df = pd.read_csv("https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv",sep=';')

df.to_sql("airports",'sqlite:///airports.sqlite',if_exists="replace",dtype={"column_1": sq.BIGINT,"column_2": sq.TEXT,"column_3": sq.TEXT,"column_4": sq.TEXT,"column_5": sq.TEXT,"column_6": sq.TEXT,"column_7": sq.FLOAT,"column_8": sq.FLOAT,"column_9": sq.BIGINT,"column_10": sq.FLOAT,"column_11": sq.TEXT,"column_12": sq.TEXT,"geo_punkt": sq.TEXT},index=False)