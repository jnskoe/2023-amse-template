import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy

def main():
    
    for i in range(1,13):
        num = str(i)
        if len(num) == 1:
            num = "0"+num    
        df = pd.read_csv("https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100031297/2019-"+num+".csv")

        df.to_sql("Monthdata"+num,'sqlite:///data.sqlite',if_exists="replace")


    df = pd.read_csv("/home/wicket/Downloads/stundenwerte_TF_01766_19891001_20221231_hist/produkt_tf_stunde_19891001_20221231_01766.txt",sep=";")

    df.to_sql("weather",'sqlite:///data.sqlite',if_exists="replace")


    monthdata = []
    for i in range(1,13):
        num = str(i)
        if len(num) == 1:
            num = "0"+num 
        
        df = pd.read_sql_table('Monthdata'+num, 'sqlite:///data.sqlite')
        for index, row in df.iterrows():
            monthdata.append((datetime.strptime(row["Datetime"], "%Y-%m-%d %H:%M"),row["100031297 (Promenade)"]))

    weatherdata = []
    df = pd.read_sql_table('weather', 'sqlite:///data.sqlite')
    for index, row in df.iterrows():
        weatherdata.append((datetime.strptime(str(row["MESS_DATUM"]),"%Y%m%d%H"),row["RF_STD"]))
    
    currdate = monthdata[0][0]
    combinedmonth = []
    sum = 0
    for i in monthdata:
        if i[0].hour == currdate.hour:
            sum = sum + i[1]
        else:
            combinedmonth.append((currdate,sum))
            sum = i[1]
            currdate  = i[0]
    cleanedweatherdata = []
    for i in weatherdata:
        if str(i[0].year) == "2019":
            cleanedweatherdata.append(i)
    zip(*combinedmonth)
    plt.plot(*zip(*combinedmonth))
    zip(*cleanedweatherdata)
    plt.plot(*zip(*cleanedweatherdata))
    plt.show()
   
if __name__ == "__main__":
    main()