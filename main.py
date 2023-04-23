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
                'quantity': mass,
                'measure': unit
            })
        file.readline()
        food[dish] = all_food
    print(food)
