import pandas as pd
import sqlalchemy as sq
df = pd.read_csv("https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv",sep=";")

df.to_sql("airports",'sqlite:///airports.sqlite',if_exists="replace",dtype={"column_1": sq.INTEGER,"column_2": sq.TEXT})