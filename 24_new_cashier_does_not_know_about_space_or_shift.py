'''
New Cashier Does Not Know About Space or Shift

ex. 
milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza --> Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke
pizzachickenfriesburgercokemilkshakefriessandwich --> Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke
'''

def get_order(order):

	menu = {1: 'burger', 2: 'fries', 3: 'chicken', 4: 'pizza', 5: 'sandwich', 6: 'onionrings', 7: 'milkshake', 8: 'coke'}
	order_item = [[v.capitalize()]*order.count(v) for k, v in menu.items() if v in order]

	return ' '.join(sum(order_item, []))

s = 'milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza'

