import requests
from bs4 import BeautifulSoup
from diet_analizing_logging_data import body_data
import locale

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

    return sorted(shopping_list, key=lambda item: locale.strxfrm(item.name))


all_ingredients_for_meals = []

breakfasts = []
second_breaksfast = []
dinner = []
supper = []

plik = open('list_meals.txt', 'w')
for index, meal in enumerate(meals):
    meal_type = meal.find_all(class_='meal-type-name')
    # ta klasa znajduje się w klasie 'carousel-content tile-element dish-element' - obiekt meals

    if meal_type[0].text == "Śniadanie":
        meal_name = meal.find_all(class_='single-position link-position')
        breakfasts.append((index, meal_name[0].text))

    if meal_type[0].text == "II śniadanie":
        meal_name = meal.find_all(class_='single-position link-position')
        second_breaksfast.append((index, meal_name[0].text))

    if meal_type[0].text == "Obiad":
        meal_name = meal.find_all(class_='single-position link-position')
        dinner.append((index, meal_name[0].text))

    if meal_type[0].text == "Kolacja":
        meal_name = meal.find_all(class_='single-position link-position')
        supper.append((index, meal_name[0].text))

    create_recipe_link()

    response3 = s.get(create_recipe_link(), headers={'X-Requested-With': 'XMLHttpRequest'})
    # print(response3.json())  # obiekt json to słownik
    json_object = response3.json()['params']

    all_ingredients_for_meals += create_ingredients_list_for_meal(json_object['products'])

lists_of_meals(breakfasts)
lists_of_meals(second_breaksfast)
lists_of_meals(dinner)
lists_of_meals(supper)

# shopping_list = create_shopping_list(all_ingredients_for_meals)
# print(*shopping_list, sep="\n")