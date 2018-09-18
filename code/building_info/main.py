from classify_hot_place import *
import pandas as pd

jongro = pd.read_csv('building/jongro.csv', encoding='cp949')

jongro = make_area_column(jongro)
jongro_detail = make_group_detail(jongro)

# too calm to be hot
too_calm = get_too_calm(jongro_detail)
already_hot = get_already_hot(jongro_detail) - too_calm
candidates = get_candidates(jongro_detail, too_calm, already_hot)

print(len(too_calm), len(already_hot), len(candidates))
