def colores(*args):
	print('El color', args[0], 'es mi favorito.', 'El color', args[1], 'tampoco está mal.')

colores('amarillo', 'blanco')

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(10, 6, 34, 3, 90, 67)
