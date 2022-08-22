import pandas as pd
from konlpy.tag import Mecab

mecab = Mecab()

df = pd.read_csv('/result/recipe_name_ingredient.csv', index_col = 0)
uniq_recipe_list = df['recipe_name'].unique()

for recipe_name in uniq_recipe_list:

    df = df[df['recipe_name'] == recipe_name]
    uniq_ingredient_list = df['ingredient'].unique()

    ingredient_morphs_list = []
    ingredient_pos_list = []

    for ingredient_name in uniq_ingredient_list:

        ingredient_morphs = mecab.morphs(ingredient_name)
        ingredient_pos = mecab.pos(ingredient_name)

        ingredient_morphs_list.append(ingredient_morphs)
        ingredient_pos_list.append(ingredient_pos)

    print(ingredient_morphs_list)
    print(ingredient_pos_list)
    exit()
