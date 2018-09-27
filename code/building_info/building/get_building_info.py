import pandas as pd
import glob, os

def get_building_info():
    path = "C:\\workspace\\data_analysis\\real_estimate_rent\\Next_Hip_Place\\code\\building_info\\data\\"
    seoul_buildings = pd.DataFrame()
    for filename in os.listdir(path):
        df = pd.read_csv(path+filename, encoding='cp949')
        print(filename)
        seoul_buildings = seoul_buildings.append(df)

    seoul_buildings.to_csv('data/seoul_buildings.csv', encoding='utf-8')
