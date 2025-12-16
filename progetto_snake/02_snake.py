#Ogni tupla è una cella del corpo
#Rappresenta il serpente come lista di tuple di celle di griglia (i,j)
#Crea una nuova testa a destra dell'attuale (aggiungila all'inizio come insert)
#Rimuovi l'ultima cella (pop)
#Stampa

#Creo il corpo
corpo=[
    (0,0),
    (20,0),
    (40,0)
]

#Creo la testa
testa=[
    (60,0)
]

#Aggiornamento del movimento

#Aggiungo la testa al primo elemento di 'corpo'
corpo.insert(0, testa)

#Tolgo l'ultimo elemento con pop()
corpo.pop()


print(corpo)