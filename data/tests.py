import pandas as pd
from pandas.testing import assert_frame_equal
import script


def test():
    df1 = pd.read_sql_table('weather', 'sqlite:///data.sqlite',columns=["STATIONS_ID","MESS_DATUM","QN_8","ABSF_STD","VP_STD","TF_STD","P_STD","TT_STD","RF_STD","TD_STD","eor"])
    df2 = pd.read_sql_table('Monthdata01', 'sqlite:///data.sqlite')
    #df1test = pd.DataFrame({"index":range(290701),"STATIONS_ID":range(290701),"MESS_DATUM":range(290701),"QN_8":range(290701),"ABSF_STD":range(290701),"VP_STD":range(290701),"TF_STD":range(290701),"P_STD":range(290701),"TT_STD":range(290701),"RF_STD":range(290701),"TD_STD":range(290701),"eor":range(290701)})
    df1test = pd.read_csv("/home/wicket/Downloads/stundenwerte_TF_01766_19891001_20221231_hist/produkt_tf_stunde_19891001_20221231_01766.txt",sep=";")
    pd.testing.assert_frame_equal(df1, df1test,check_index_type=False)