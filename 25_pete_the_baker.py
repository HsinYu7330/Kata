'''
Pete, the baker

ex. 
cakes(recipes, ingredients)
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
--> 2
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
--> 0
'''

def cakes(recipe, available):
    cnt = []
    for material in recipe.keys():
        
        try:
            cnt.append(available[material]/recipe[material])
        except:
            cnt.append(0)
        
    return int(min(cnt))