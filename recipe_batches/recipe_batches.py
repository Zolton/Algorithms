#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # x = recipe.values()
  # print("Recipes: ", recipe.values()) 
  # print("Ingredients: ", ingredients) 
  #my_dict ={"java":100, "python":112, "c":11} 
  
# list out keys and values separately 
  recipeKeys = list(recipe.keys()) 
  recipeValues = list(recipe.values()) 
  ingredientsKeys = list(ingredients.keys()) 
  ingredientsValues = list(ingredients.values()) 
  print(recipeKeys)
  print(recipeValues)
  print(ingredientsKeys)
  print(ingredientsValues)
  count = 0
  if recipeKeys != ingredientsKeys:
    return 0
  else:
    for i in recipeValues:
      for j in ingredientsValues:
        print("thi sis i: ", i)
        print("thi sis j: ", j)
        # if ingredientsValues[i] / recipeValues[i] <= 0:
        #   return count
        if j/i > 0:
          count = count + 1
          print("test", count)
  return count
  
    # for x in 
    #   print("There's enough")
  # for x in recipe:
  #   # if recipe.values() >= ingredients.values():
  #   print("Name is ", x.values())
  #   print("value is ", x.keys())
  #   for i in ingredients:
  #     print(i)
  #     if x > i:
  #       print(str(x) + "is greater than " + str(i) + " ok")
  #     if x < i:
  #       print(str(x) + "is not greater than " + str(i) + "not ok")
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))