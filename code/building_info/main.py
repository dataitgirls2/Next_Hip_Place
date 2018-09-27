from classify_hot_place import *
import pandas as pd

# get data
seoul_buildings = pd.read_csv('data/seoul_buildings.csv', encoding='utf-8')
seoul_buildings = make_area_column(seoul_buildings)
seoul_detail = make_group_detail(seoul_buildings)

seoul_rent = pd.read_csv('data/seoul_rent.csv', encoding='utf-8')
seoul_sns = pd.read_csv('data/seoul_sns.csv')

# classify
too_calm = get_too_calm(seoul_detail)
already_hot = get_already_hot(seoul_detail) - too_calm
too_expensive = get_too_expensive(seoul_rent) - already_hot - too_calm
candidates = get_candidates(seoul_detail, too_calm, already_hot, too_expensive)

# make geojson with class
geojson = json.load(open('data\seoul_dong.geojson', encoding='utf-8'))
geojson_building_class = make_geojson(geojson, too_calm, already_hot, candidates)
save_geojson(geojson_building_class, 'data/seoul_class_building.geojson')

# check number of classes
print(len(too_calm))
print(len(already_hot))
print(len(candidates))
print(too_calm)
