x = 0

while x <= 30:
	x += 1
	if x == 4 or x == 6 or x ==10: 
		print('Se salto el valor', x , 'de x')
		continue
		

	if x == 15: 
		print('se rompio la ejecucion')
		break
		x += 1
	print(x)