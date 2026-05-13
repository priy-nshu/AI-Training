import pandas as pd
import numpy as np

def PandaBasics():
    df=pd.read_csv('../Python Sample Dataset/housing.csv',header=None,nrows=10)
    print(df)
    df2=pd.read_excel('../Python Sample Dataset/housing.xlsx',nrows=10)
    print(df2)

    print(df.head(2))
    print(df.tail(1))

def write2_file():
    data={'Name':['C','Sharp','Corner'],'Age':[20,21,22],'Address':['Delhi','Kanpur','Tamil Nadu']}
    df=pd.DataFrame(data)
    df.to_csv('../Python Sample Dataset/Creation1.csv')
    df.to_excel('../Python Sample Dataset/Creation2.csv')


########################################################
PandaBasics()
write2_file()