"""Baking Cookies"""
"""Darin Wong EECS 183 project via Python"""
import math
while True:
	people = input('How many people do you need to serve? ')
	if people.isdigit() == False:
		print('Input the correct amount of people!! No half-people please...')
	else:
		break

print('\n')
batches = int(people) / 12
if batches == 1:
	print('You will need to bake 1 batch of cookies!')
else:
	print('You will need to bake ' + str(math.ceil(batches)) + ' batches of cookies!')

print('\n')
print('Ingredients Used:')
flour1 = 2.75*batches
g_sugar1 = .75*batches
b_sugar1 = .75*batches
butter1 = .5*batches
c_cheese1 = .5*batches
eggs1 = 2*batches
vanilla1 = 2*batches
c_chips1 = 2*batches
b_powder1 = 1*batches
b_soda1 = .5*batches
salt1 = .5*batches
if flour1 == 1:
	print('Flour: 1 Cup')
else:
	print('Flour: ' + str(round(flour1,2)) + ' Cups')
if g_sugar1 == 1:
	print('Granulated Sugar: 1 Cup')
else:
	print('Granulated Sugar: ' + str(round(g_sugar1,2)) + ' Cups')
if b_sugar1 == 1:
	print('Brown Sugar: 1 Cup')
else:
	print('Brown Sugar: ' + str(round(b_sugar1,2)) + ' Cups')
if butter1 == 1:
	print('Butter: 1 Cup/Stick')
else:
	print('Butter: ' + str(round(butter1,2)) + ' Cups/Sticks')
if c_cheese1 == 1:
	print('Cream Cheese: 1 Cup')
else:
	print('Cream Cheese: ' + str(round(c_cheese1,2)) + ' Cups')
if eggs1 == 1:
	print('Eggs: 1 Egg')
else:
	print('Eggs: ' + str(round(eggs1,2)) + ' Eggs')
if vanilla1 == 1:
	print('Vanilla: 1 Teaspoon')
else:
	print('Vanilla: ' + str(round(vanilla1,2)) + ' Teaspoons')
if c_chips1 == 1:
	print('Chocolate Chips: 1 Cup')
else:
	print('Choclate Chips: ' + str(round(c_chips1, 2)) + ' Cups')
if b_powder1 == 1:
	print('Baking Powder: 1 Teaspoon')
else:
	print('Baking Powder: ' + str(round(b_powder1,2)) + ' Teaspoons')
if b_soda1 == 1:
	print('Baking Soda: 1 Teaspoon')
else:
	print('Baking Soda: ' + str(round(b_soda1,2)) + ' Teaspoons')
if salt1 == 1:
	print('Salt: 1 Teaspoon')
else:
	print('Salt: ' + str(round(salt1,2)) + ' Teaspoons')

print('\n')
while True:
	shopping = str(input('Create shopping list? (yes/no)'))
	if shopping == 'no':
		print('Good luck!')
		exit()
	elif shopping == 'yes':
		print('Shopping List for "Best Ever" Chocolate Chip Cookies')
		print('----------------------------------------------------')
		flour = math.ceil((2.75*batches)/20)
		g_sugar = math.ceil((.75*batches)/10)
		b_sugar = math.ceil((.75*batches)/4.5)
		butter = math.ceil((.5*batches)/2)
		c_cheese = math.ceil((.5*batches)/1)
		eggs = math.ceil((2*batches)/12)
		vanilla = math.ceil((2*batches)/12)
		c_chips = math.ceil((2*batches)/2)
		if flour == 1:
			print('1 Bag of Flour')
		else:
			print(str(flour) +' Bags of Flour')
		if g_sugar == 1:
			print('1 Bag of Granulated Sugar')
		else:
			print(str(g_sugar) +' Bags of Granulated Sugar')
		if b_sugar == 1: 
			print('1 Bag of Brown Sugar')
		else:
			print(str(b_sugar) +' Bags of Brown Sugar')
		if butter == 1:
			print('1 Lb of Butter')
		else:
			print(str(butter) +' Lbs of Butter')
		if c_cheese == 1:
			print('1 8oz Box of Cream Cheese')
		else:
			print(str(c_cheese) +' 8oz Boxes of Cream Cheese')
		print(str(eggs) +' Dozen Eggs')
		if vanilla == 1:
			print('1 Bottle of Vanilla')
		else:
			print(str(vanilla) +' Bottles of Vanilla')
		if c_chips == 1:
			print('1 12oz Bag of Dark Chocolate Chips')
		else:
			print(str(c_chips) +' 12oz Bags of Dark Chocolate Chips')

		print('\n')
		print('Total Expected Cost of Ingredients: ')
		cost = flour* 2.69 + g_sugar*3.99 + b_sugar*2.29 + butter*2.79 + c_cheese*2.49 + eggs*1.99 + vanilla*6.79 + c_chips*2.39
		price = round(cost, 2)
		print('$' + str(price))

		print('\n')
		print("Have a great party!!! Don't get too lit!!!")
		break
	else:
		print('?? Please input "yes" or "no": ')