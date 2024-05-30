import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
overweight = []
for i in range(len(df)):
    bmi = df['weight'][i]/((df['height'][i]/100) ** 2)
    if bmi > 25:
        overweight.append(1)
    else:
        overweight.append(0)

df['overweight'] = overweight

# 3
df['cholesterol'].where(df['cholesterol'] == 1, 0)
df['gluc'].where(df['gluc'] == 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], value_vars = ['cardio'])

    # 6
    df_cat = 
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
