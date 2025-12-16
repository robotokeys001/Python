#Sono come liste
#Ma non si possono modificare
#Si scrivono con ()
punto=(10,20)

#Accesso a tuple
print(punto[0])
print(punto[1])

#Unpacking
x,y = punto
print(x)
print(y)

#Non si puo fare
#punto [0] = 50 mi dara errore

#Perche si utilizzano
#Sicure-->Non modificabili
#Veloci
#Utili per rappresentare posizioni(x,y)

tupla=(1,2,3)
#Posso anche non assegnare tutti i valori tramite * Posso assegnare piu valori alla stessa variabile
x, *y=tupla

print(x, y)