### The beginnings of learning web scraping.

These are my first attempts, with notes in the comments to help me put it all together.
The program is intended to be used to extract data from a dietitian's diet website 
in a form that suits me better than those presented on the website.
Unfortunately, you are not able to test whether it works properly because 
you do not have my login and password.
You can only read my code.

### Program operation:
1. logging: post query with login data
2. page download: get query
3. processing the content of the page into an object that can be analyzed - using BeautigulSoup
4. creating list meals: list of elements from class carousel-content tile-element dish-element 
from website
5. creating a shopping list by iterate through meals:
* creating lists of names from different types of meals 
(breakfasts, second_breakfast, dinner, super) and saving them to file list_meals.txt
* creating list of object of class Ingredient for chosen meals
* creating one list of all ingredients for chosen meals by adding previous lists
* creating shopping list from list of all ingredients from chosen meals - 
if object exists in the list, the program change the amount of them, if it does not exist, 
add to list 


