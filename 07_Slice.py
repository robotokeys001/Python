# I due punti indicano un intervallo aperto, quindi l'elemento all'indice finale non è incluso.
numeri=[5,10,15,20,25,30]

#Stampo i primi tre
print(numeri[:3])

#Stampo gli ultimi due
print(numeri[-2:])

#Stampo gli indici pari: 0, 2 e 4
print(numeri[::2])

#Copia liste con slice
#Utile quando non vogliamo modificare l'originale
copia= numeri[:]
print(copia)

#---------------------------------------------

#TODO
#Crea una lista
#Copia la lista con slice
#Modifica un campo della lista
#Stampa le due liste a confronto
lista_numeri=[2,4,6,8,10]
copia_lista_numeri= lista_numeri[:]
copia_lista_numeri[2] = 1
print(f'La lista originale: {lista_numeri} \nlista modificata: {copia_lista_numeri}')
