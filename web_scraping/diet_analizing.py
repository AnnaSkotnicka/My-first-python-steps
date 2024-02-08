import requests
from bs4 import BeautifulSoup
from diet_analizing_logging_data import body_data

s = requests.Session()

url = "https://pacjent.dietetykpro.pl/zaloguj"

response1 = s.post(url, data=body_data)

main_link = 'https://pacjent.dietetykpro.pl'
response2 = s.get(main_link + '/moj-jadlospis/tydzien')

page = BeautifulSoup(response2.text, 'html.parser')
# przetwarza tekst z kodu HTML na obiekt w pamięci, który można analizować
# zwraca bs4.element.ResultSet (w jednoelementowej liście) - w konsoli kod HTLM
meals = page.find_all(class_='carousel-content tile-element dish-element')
# zwraca bs4.element.ResultSet dla szukanej klasy
# print("meals", meals[7].get_text())


class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit


# Wyświetlanie listy wszystkich śniadań
def lists_of_breakfasts(m, m_type):
    if m_type[0].text == "Śniadanie":
        breakfast = m.find_all(class_='single-position link-position')
        print(breakfast[0].text)  # Lista śniadań


def create_recipe_link():
    breakfast_link = (meal.find("a"))['href']
    link = main_link + breakfast_link
    return link


def create_ingredients_list_for_meal(products):
    all_ingredients = []
    for product in products:
        product_information = Ingredient(name=product['name'],
                                         amount=float(product['size']) * float(json_object['element']['size']),
                                         unit="g")
        all_ingredients.append(product_information)
    return all_ingredients


def find_in_shopping_list(ingridient, shopping_list):
    for i in shopping_list:
        if i.name == ingridient.name:
            return i
    return None


def create_shopping_list(all_ingredients):
    shopping_list = []
    for ingredient in all_ingredients:
        na_liscie_zakupow = find_in_shopping_list(ingredient, shopping_list)
        if na_liscie_zakupow:
            na_liscie_zakupow.amount += ingredient.amount
        else:
            shopping_list.append(ingredient)

    return shopping_list


all_ingredients_for_meals = []
for meal in meals:
    meal_type = meal.find_all(class_='meal-type-name')
    # ta klasa znajduje się w klasie 'carousel-content tile-element dish-element' - obiekt meals
    # lists_of_breakfasts(meal, meal_type)
    create_recipe_link()

    response3 = s.get(create_recipe_link(), headers={'X-Requested-With': 'XMLHttpRequest'})
    # print(response3.json())  # obiekt json to słownik
    json_object = response3.json()['params']

    all_ingredients_for_meals += create_ingredients_list_for_meal(json_object['products'])

shoping_list = create_shopping_list(all_ingredients_for_meals)


def display():
    alphabetical_list = []
    for ingredient in shoping_list:
        alphabetical_list.append([ingredient.name, ingredient.amount, ingredient.unit])
    return sorted(alphabetical_list)
    # return sorted(shoping_list, key=lambda item: item.name)


print(*display(), sep="\n")
