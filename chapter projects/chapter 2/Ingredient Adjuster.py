# A simple program that will list the ingredients of a recipe depending on how many servings the user requests

# Website URL for recipe: https://www.allrecipes.com/recipe/45396/easy-pancakes/

# Set ingredients and their respective quantities needed for the base servings within a dictionary.
base_servings = 4
recipe = {
    "cup(s) of flour": 1,
    "tablespoon(s) of sugar": 2,
    "teaspoon(s) of baking power": 2,
    "teaspoon(s) of salt": 1,
    "egg(s) beaten": 1,
    "cup(s) of milk": 1,
    "tablespoon(s) of vegetable oil":  2
}

# Request how many servings the user would want
print("Hello, today we are making 'easy pancakes'!")
servings_wanted = int(input("How many servings do you want to make? "))
print("\n")

# Calculate how much of each ingredient the user will need
multiplier = servings_wanted / base_servings

# Loop through the dictionary and print out how much of each ingredient we need to 1 decimal place
print("For " + str(servings_wanted) + " serving(s), you will need:")
for ingredient in recipe:
    print(str(format(recipe[ingredient] * multiplier, '.1f')) + " " + ingredient)
