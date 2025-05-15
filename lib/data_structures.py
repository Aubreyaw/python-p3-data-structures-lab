spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        emoji = "🌶" * food["heat_level"]
        print (f"{name} ({cuisine}) | Heat Level: {emoji}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        emoji = "🌶" * food["heat_level"]
        if food["heat_level"] > 5:
            print(f"{name} ({cuisine}) | Heat Level: {emoji}")
    pass

def get_average_heat_level(spicy_foods):
    total = sum([food["heat_level"]for food in spicy_foods]) 
    count = len(spicy_foods)  
    return int(total/count)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food) 
    return spicy_foods
    pass
