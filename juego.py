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



def imprimirLista(lista):
	if len(lista) == 1:
		return str(lista[0])
	else:
		return str(lista[0]) +" "+str(imprimirLista(lista[1:]))



def imprimirmatriz(matriz):
	if len(matriz) == 1:
		return str(imprimirLista(matriz[0]))
	else:
		return str(imprimirLista(matriz[0]))+"\n"+str(imprimirmatriz(matriz[1:]))






def revisarVecinos(matriz, pos): ##Revision de los vecinos de cada posicion
 	
 	vecinos = 0
 	if pos == (0,0):
 		for k in matriz[0:pos[0]+2]:
 			for j in k[0:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 
 	elif pos[0] == 0:
 		for k in matriz[0:pos[0]+2]:
 			for j in k[pos[1]-1:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 
 	elif pos[1] == 0:
 		for k in matriz[pos[0]-1:pos[0]+2]:
 			for j in k[0:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 	
 	else:
 		for k in matriz[pos[0]-1:pos[0]+2]:
 			for j in k[pos[1]-1:pos[1]+2]:
 				if j == 1:
 					vecinos+=1
 
 
	if(matriz[pos[0]][pos[1]] == 1):
		vecinos = vecinos -1
 
 	
 	return vecinos


def nuevaGeneracion(matriz):
	vecinosVivos = 0 				
	resultado = np.zeros_like(matriz)
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			vecinosVivos = revisarVecinos(matriz,(i,j))
			if matriz[i][j] == 0 and vecinosVivos == 3:
				resultado[i][j] = 1
			elif matriz[i][j] == 1 and vecinosVivos < 2:
				resultado[i][j] = 0
			elif matriz[i][j] == 1 and vecinosVivos > 3:
				resultado[i][j] = 0
			elif matriz[i][j] == 1 and (vecinosVivos == 2 or vecinosVivos == 3):
				resultado[i][j] = 1

	print imprimirmatriz(resultado)
	print "--------------------------"
	print "\n"
	raw_input('Presione enter para continuar:')	
	os.system("clear")	
	nuevaGeneracion(resultado)
 
		
print imprimirmatriz(a)
print "--------------------------"
print "\n"
nuevaGeneracion(a)