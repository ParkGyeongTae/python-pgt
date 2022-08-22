import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

##################################################################
# 만개의 레시피 홈페이지의 랭킹 페이지에서 100개의 레시피 url을 리스트로 가져온다. #
##################################################################

def get_ranking_recipe_url(output_format):

    ranking_url = 'https://www.10000recipe.com/ranking/home_new.html'
    get_request = requests.get(ranking_url)

    if get_request.status_code == 200:
        request_content = get_request.content
    else:
        print(get_request.status_code)
        exit()

    page_html = BeautifulSoup(request_content, 'html.parser')
    page_html_select_one = page_html.select_one('ul.common_sp_list_ul')
    page_html_select = page_html_select_one.select('li > div > a')

    recipe_url_list = []

    for recipe_url in page_html_select:
        recipe_url_href = recipe_url.attrs['href']
        recipe_url_list.append(recipe_url_href)

    if (output_format == 'print'):
        print(recipe_url_list)
        exit()

    elif (output_format == 'return'):
        return recipe_url_list

    else:
        print('output_format을 다시 확인하세요.')
        exit()

###################################
# 각 레시피 url별 제목과 재료를 가져온다. #
###################################

def get_recipe_name_ingredient_list(recipe_list, is_tqdm, output_format):

    base_url = 'https://www.10000recipe.com'

    df_result = pd.DataFrame()

    if is_tqdm:
        num_recipes = tqdm(range(len(recipe_list)))
    else:
        num_recipes = range(len(recipe_list))

    for num_recipe in num_recipes:

        # if (num_recipe != 0):
        #     continue

        recipe_url = base_url + recipe_list[num_recipe]
        get_recipe_request = requests.get(recipe_url)

        if get_recipe_request.status_code == 200:
            recipe_page_content = get_recipe_request.content

        else:
            print(get_recipe_request.status_code)
            exit()

        recipe_html = BeautifulSoup(recipe_page_content, 'html.parser')
        recipe_name = recipe_html.select_one('div.view2_summary')
        recipe_name = recipe_name.select_one('h3')
        recipe_name = recipe_name.get_text()

        recipe_ingredients_list = recipe_html.select_one('div.ready_ingre3')
        recipe_ingredients_list = recipe_ingredients_list.select('ul > a')

        ingredients_list = []

        for ingredient in recipe_ingredients_list:

            ingredient_text = ingredient.get_text()

            ingredient_text = ingredient_text.split('\n')
            ingredient_text = [word.strip() for word in ingredient_text]
            ingredient_text = list(filter(None, ingredient_text))
            ingredient_text.remove('구매')

            ingredients_list.append(ingredient_text)

        ingredients_list = list(filter(None, ingredients_list))

        df = pd.DataFrame(ingredients_list)

        df.columns = ['ingredient', 'detail']
        df.fillna('-1', inplace = True)
        df['recipe_name'] = recipe_name

        df = df[['recipe_name', 'ingredient', 'detail']]

        df_result = pd.concat([df_result, df], axis = 0, ignore_index = True)

    if (output_format == 'print'):
        print(df_result)
        exit()
    elif (output_format == 'return'):
        return df_result
    elif (output_format == 'csv'):
        df_result.to_csv('/result/recipe_name_ingredient.csv')
        exit()
    else:
        print('output_format을 다시 확인하세요.')
        exit()


if __name__ == '__main__':

    # get_ranking_recipe_url(output_format = 'print')
    # exit()

    recipe_list = get_ranking_recipe_url(output_format = 'return')

    get_recipe_name_ingredient_list(recipe_list   = recipe_list, 
                                    is_tqdm       = True,
                                    output_format = 'print')

    exit()