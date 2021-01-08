z = True
while z:
	other = float(input('Help = 1 / Quitter = 0: '))

	if other == 1:
		print('---------------------')
		print('to String = 2')
		print('to Float = 3')
		print('to Int = 4')
		print('---------------------')
	elif other == 2:
		a = str(input('Veuillez entrez une valeur: '))
		print("<value '" + a + "'>")
		print(type(a))
	elif other == 3:
		a = float(input('Veuillez entrez une valeur: '))
		print("<value '" + a + "'>")
		print(type(a))
	elif other == 4:
		a  = int(input('Veuillez entrez une valeur: '))
		print("<value '" + a + "'>")
		print(type(a))
	elif other == 0:
		z = False