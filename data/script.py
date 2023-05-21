import pandas as pd

#df = pd.read_csv("https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100031297/2019-01.csv")

#df.to_sql("Monthdata",'sqlite:///data.sqlite')

df = pd.read_csv("/home/wicket/Downloads/stundenwerte_TF_01766_19891001_20221231_hist/produkt_tf_stunde_19891001_20221231_01766.txt",sep=";")

df.to_sql("weather2",'sqlite:///data.sqlite')