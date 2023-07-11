import urllib.request
import zipfile
import pandas as pd
import os
from pathlib import Path
import sqlalchemy as sq

def valid(input):
    return int(input) == 2001

def valcor(input):
    return float(input) >= -90 and float(input) <= 90

def valstr(input):
    if input == "":
        return False
    return True

if __name__ == '__main__':
    url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
    dataname = Path(url).stem
    zip_name = dataname +'.zip'
    extract_path = os.path.join(os.curdir, dataname)
    urllib.request.urlretrieve(url,zip_name)
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zip_name)

    datafilename = "stops.txt"
    df = pd.read_csv(os.path.join(extract_path, datafilename),
                     sep = ",",
                     index_col = False,
                     usecols = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"])
    
    df = df[df["zone_id"].apply(lambda x: valid(x))]
    df = df[df["stop_lat"].apply(lambda x: valcor(x))]
    df = df[df["stop_lon"].apply(lambda x: valcor(x))]
    df = df[df["stop_name"].apply(lambda x: valstr(x))]
    
    
    
    
    
    df.to_sql("stops",'sqlite:///gtfs.sqlite',if_exists="replace",index = False, dtype={
    "stop_id": sq.BIGINT,
    "stop_name": sq.TEXT,
    "stop_lat": sq.FLOAT, 
    "stop_lon": sq.FLOAT,
    "zone_id": sq.BIGINT
    })
    
    