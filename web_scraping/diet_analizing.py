import requests
from bs4 import BeautifulSoup
from diet_analizing_logging_data import body_data
import locale
import re

locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")

s = requests.Session()

# logowanie
url = "https://pacjent.dietetykpro.pl/zaloguj"
response1 = s.post(url, data=body_data)

# odpowiedź przeglądarki z podanego adresu
main_link = 'https://pacjent.dietetykpro.pl'
response2 = s.get(main_link + '/moj-jadlospis/tydzien')

# przetworzenie odpowiedzi na obiekt w pamięci, który można analizować (BeautifulSoup)
page = BeautifulSoup(response2.text, 'html.parser')
# zwraca bs4.element.ResultSet (w jednoelementowej liście) - w konsoli kod HTLM

meals = page.find_all(class_='carousel-content tile-element dish-element')
# zwraca bs4.element.ResultSet dla szukanej klasy
# print("meals", meals[7].get_text())


class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return f'{self.name} {self.amount} {self.unit}'


# zapisywanie do pliku listy posiłków danego typu wraz z indeksem
def lists_of_meals(meal_list: list):
    for number, name in meal_list:
        plik.write(str(number) + ' ' + name + "\n")
    plik.write("\n")


def create_recipe_link(m):
    dish_link = m.find("a")['href']
    return main_link + dish_link


def create_ingredients_list_for_meal(meal):
    dishes = meal.find_all(class_='single-position')

    all_ingredients = []
    unit = {1: "ml", 2: "g"}
    for dish in dishes:
        if 'link-position' in dish['class']:
            response3 = s.get(create_recipe_link(dish), headers={'X-Requested-With': 'XMLHttpRequest'})
            # print(response3.json())  # obiekt json to słownik
            json_object = response3.json()['params']
            products = json_object['products']

            for product in products:
                product_information = Ingredient(name=product['name'],
                                                 amount=float(product['size']) * float(json_object['element']['size']),
                                                 unit=unit[int(product['type'])])
                all_ingredients.append(product_information)
        else:
            dish_elements = re.search(r'^([\w ]+) \((\d+) (\w+)\)$', dish.text)

            product_information = Ingredient(name=dish_elements.group(1),
                                             amount=float(dish_elements.group(2)),
                                             unit=dish_elements.group(3))
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

    return sorted(shopping_list, key=lambda item: locale.strxfrm(item.name))


all_ingredients_for_meals = []

breakfasts = []
second_breaksfast = []
dinner = []
supper = []

#  Wpisać indeksy z pliku list_meals.txt -> utworzy się lista zakupów dla wybranych produktów
indexes = [6, 10]

plik = open('list_meals.txt', 'w')
for index, meal in enumerate(meals):
    meal_type = meal.find_all(class_='meal-type-name')
    # ta klasa znajduje się w klasie 'carousel-content tile-element dish-element' - obiekt meals

    if meal_type[0].text == "Śniadanie":
        dish_names = meal.find_all(class_='single-position link-position')
        for dish_name in dish_names:
            breakfasts.append((index, dish_name.text))

    if meal_type[0].text == "II śniadanie":
        dish_names = meal.find_all(class_='single-position link-position')
        for dish_name in dish_names:
            second_breaksfast.append((index, dish_name.text))

    if meal_type[0].text == "Obiad":
        dish_names = meal.find_all(class_='single-position link-position')
        for dish_name in dish_names:
            dinner.append((index, dish_name.text))

    if meal_type[0].text == "Kolacja":
        dish_names = meal.find_all(class_='single-position link-position')
        for dish_name in dish_names:
            supper.append((index, dish_name.text))

    if index not in indexes:
        continue

    all_ingredients_for_meals += create_ingredients_list_for_meal(meal)

lists_of_meals(breakfasts)
lists_of_meals(second_breaksfast)
lists_of_meals(dinner)
lists_of_meals(supper)
plik.close()

shopping_list = create_shopping_list(all_ingredients_for_meals)
print(*shopping_list, sep="\n")

# Podwajanie porcji
# dopisać w nawiasie co do jakiego przepisu??
# dopisać przelicznik w sztukach??
