#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipeKeys = list(recipe.keys()) 
  recipeValues = list(recipe.values()) 
  ingredientsKeys = list(ingredients.keys()) 
  ingredientsValues = list(ingredients.values()) 
  count = []
  if recipeKeys != ingredientsKeys:
    return 0
  else:
    for i in range(0, len(recipeValues)):
      test = ingredientsValues[i] / recipeValues[i]
      if test > 1:
        count.append(round(test))
  return min(count)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))