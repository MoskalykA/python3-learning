other = int(input('Diviser = 1 / Multiplier = 2 / Additionner = 3 / Soustraction = 4: '))

if other == 1:
	a = int(input('Premier nombre a diviser: '))
	b = int(input('Deuxième nombre a diviser: '))
	print(a / b)
elif other == 2:
	a = int(input('Premier nombre a multiplier: '))
	b = int(input('Deuxième nombre a multiplier: '))
	print(a * b)
elif other == 3:
	a = int(input('Premier nombre a additionner: '))
	b = int(input('Deuxième nombre a additionner: '))
	print(a + b)
elif other == 4:
	a = int(input('Premier nombre a soustraire: '))
	b = int(input('Deuxième nombre a soustraire: '))
	print(a - b)