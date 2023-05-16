import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100031297/2019-01.csv")

df.to_sql("Monthdata",'sqlite:///data.sqlite')