from pprint import pprint


def create_cook_book(file_name):

    with open(file_name, 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish] = ingredients

    pprint(cook_book, sort_dicts=False)
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):

    cook_book = create_cook_book('recipes.txt')
    shopping_list = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            quantity = 0
            if shopping_list.get(ingredient['ingredient_name']) is not None:
                quantity = int(shopping_list[ingredient['ingredient_name']]
                               ['quantity'])
            shopping_list[ingredient['ingredient_name']] = {
                'measure': ingredient['measure'],
                'quantity': (int(ingredient['quantity']) * person_count +
                             quantity)
            }

    print('\nСписок покупок:')
    pprint(shopping_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)