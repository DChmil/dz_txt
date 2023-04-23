def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop_list = dict(ingredient)
                new_shop_list['quantity'] *= person_count
                if new_shop_list['ingredient_name'] not in shop_list:
                    status = new_shop_list.pop('ingredient_name')
                    shop_list[status] = new_shop_list
                else:
                    status = new_shop_list.pop('ingredient_name')
                    shop_list[status]['quantity'] += new_shop_list['quantity']
    return shop_list

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    food = {}
    for line in file:
        dish = line.strip()
        food_count = int(file.readline().strip())
        all_food = []
        for _ in range(food_count):
            component, mass, unit = file.readline().strip().split(' | ')
            all_food.append({
                'ingredient_name': component,
                'quantity': int(mass),
                'measure': unit
            })
        file.readline()
        food[dish] = all_food
    print(food)

racion = ['Запеченный картофель', 'Омлет', 'Утка по-пекински']
stol = get_shop_list_by_dishes(racion, 3, food)
print(stol)