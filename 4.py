other = float(input('Diviser = 1 / Multiplier = 2 / Additionner = 3 / Soustraction = 4: '))

if other == 1:
	a = float(input('Premier nombre a diviser: '))
	b = float(input('Deuxième nombre a diviser: '))
	print(a / b)
elif other == 2:
	a = float(input('Premier nombre a multiplier: '))
	b = float(input('Deuxième nombre a multiplier: '))
	print(a * b)
elif other == 3:
	a = float(input('Premier nombre a additionner: '))
	b = float(input('Deuxième nombre a additionner: '))
	print(a + b)
elif other == 4:
	a = float(input('Premier nombre a soustraire: '))
	b = float(input('Deuxième nombre a soustraire: '))
	print(a - b)