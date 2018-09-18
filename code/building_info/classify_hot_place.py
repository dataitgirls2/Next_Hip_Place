import pandas as pd

# 건물건축면적 합, 비율 구하기
def make_area_column(df):
    df['cnt'] = 1
    df_area = df.groupby('법정동명')['건물건축면적'].sum().reset_index()
    df_area.columns = ['법정동명', '건물건축면적합계']
    df = df.merge(df_area, on='법정동명')
    df['면적비율'] = df['건물건축면적'] / df['건물건축면적합계'] * 100

    return df

# 세부용도로 그룹화하기
def make_group_detail(df):
    df = df.groupby(['법정동명', '주요용도명', '세부용도명'])\
            .agg({'지상층수':'mean', '지하층수':'mean', '건물높이':'mean', '건물건축면적':'sum', 'cnt':'sum', '건물건축면적합계':'mean', '면적비율':'sum'})\
            .reset_index()

    return df

# 아파트 비율
def get_apt(df_detail, percent):
    apt = df_detail.loc[(df_detail["세부용도명"] =='아파트') & (df_detail['면적비율'] > percent), '법정동명'].unique()
    return apt

# 1종근린시설 비율
def get_shops1(df, percent):
    shops_1 = df.loc[(df['주요용도명'] == '제1종근린생활시설') & (df['면적비율'] > percent), '법정동명'].unique()
    return shops_1

# 2종근린시설 비율
def get_shops2(df, percent):
    shops_2 = df.loc[(df['주요용도명'] == '제2종근린생활시설') & (df['면적비율'] > percent), '법정동명'].unique()
    return shops_2

# 업무시설 비율
def get_office(df, percent):
    office = df.loc[(df['주요용도명'] == '업무시설') & (df['면적비율'] > percent), '법정동명'].unique()
    return office

# too calm to be hot :아파트 35% 이상이거나 업무시설 50% 이상
def get_too_calm(df_detail):
    apt_35 = get_apt(df_detail, 35)
    office_50 = get_office(df_detail, 50)
    too_calm = df_detail.loc[(df_detail['법정동명'].isin(apt_35)) | (df_detail['법정동명'].isin(office_50)), '법정동명'].unique()

    return set(too_calm)

# already hot
def get_already_hot(df_main):
    # 1. 2종 근린시설이 1종 근린시설의 2배보다 많은 곳
    shop1 = df_main.loc[df_main['주요용도명']=='제1종근린생활시설', ['법정동명', '면적비율']].groupby('법정동명').sum().reset_index()
    shop1.columns = ['법정동명', '1종']
    shop2 = df_main.loc[df_main['주요용도명']=='제2종근린생활시설', ['법정동명', '면적비율']].groupby('법정동명').sum().reset_index()
    shop2.columns = ['법정동명', '2종']

    shop_all = shop1.merge(shop2, on='법정동명')
    shop_all['2종/1종비율'] = shop_all['2종'] / shop_all['1종']
    more_shop2 = shop_all.loc[shop_all['2종/1종비율'] > 1.9, '법정동명'].unique()

    hot_place1 = more_shop2

    # 1종, 2종 합쳐서 50%가 넘는 곳
    shop_all['1/2종합계'] = shop_all['1종'] + shop_all['2종']
    hot_place2 = shop_all.loc[shop_all['1/2종합계'] > 50, '법정동명'].unique()

    # 최종
    already_hot = set(hot_place1) | set(hot_place2)
    return already_hot

def get_candidates(df_main, too_calm, already_hot):
    not_candidates = set(list(too_calm) + (list(already_hot)))
    candidates = set(df_main.loc[(~df_main['법정동명'].isin(not_candidates)), '법정동명'])

    return candidates
