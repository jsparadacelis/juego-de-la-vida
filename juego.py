import numpy as np 
import os

# a = [[0,1,0],
#  	 [0,1,0],
#  	 [0,1,0]]
# deslizador
a = [[0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,1,0,0,0,0],
 	 [0,0,0,0,1,0,0,0,0,0],
 	 [0,0,0,0,1,1,1,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0]]



def imprimirTabla(tabla):
 	for k in tabla:
 		for j in k:
 			print j,
 		print
 	print "--------------------------"
	print "\n"


def revisarVecinos(tabla, pos): ##Revision de los vecinos de cada posicion
 	
 	vecinos = 0
 	if pos == (0,0):
 		for k in tabla[0:pos[0]+2]:
 			for j in k[0:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 
 	elif pos[0] == 0:
 		for k in tabla[0:pos[0]+2]:
 			for j in k[pos[1]-1:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 
 	elif pos[1] == 0:
 		for k in tabla[pos[0]-1:pos[0]+2]:
 			for j in k[0:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 	
 	else:
 		for k in tabla[pos[0]-1:pos[0]+2]:
 			for j in k[pos[1]-1:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 
 
	if(tabla[pos[0]][pos[1]] == 1):
		vecinos = vecinos -1
 
 	
 	return vecinos


def nuevaGeneracion(tabla):
	vecinosVivos = 0 				
	resultado = np.zeros_like(tabla)
	for i in range(len(tabla)):
		for j in range(len(tabla)):
			vecinosVivos = revisarVecinos(tabla,(i,j))
			if tabla[i][j] == 0 and vecinosVivos == 3:
				resultado[i][j] = 1
			elif tabla[i][j] == 1 and vecinosVivos < 2:
				resultado[i][j] = 0
			elif tabla[i][j] == 1 and vecinosVivos > 3:
				resultado[i][j] = 0
			elif tabla[i][j] == 1 and (vecinosVivos == 2 or vecinosVivos == 3):
				resultado[i][j] = 1

	imprimirTabla(resultado)	
	raw_input('Presione enter para continuar:')	
	os.system("clear")	
	nuevaGeneracion(resultado)
 
		
imprimirTabla(a)
nuevaGeneracion(a)