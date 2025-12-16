import turtle
pen = turtle.Turtle()

#Chiedi all'utente il numero di lati
def chiedi_lati():
    n_lati=int(input('Inserisci lati: '))
    return n_lati

#Chiedi all'utente la lunghezza
def chiedi_lunghezza():   
    l=int(input('Inserisci la lunghezza: '))
    return l

#Chiedi all'utente un colore
def chiedi_colore():
    colore=input('Inserisci un colore: ')
    return colore

#Chiedi all'utente la velocita di disegno
def chiedi_velocita():
    velocita=int(input('Inserisci la velocita: '))
    return velocita

#Disegna il poligono
def disegna_poligono(numero_lati: int, penna: turtle.Turtle, lunghezza: int, colore, velocita):
    angolo=360/numero_lati
    
    penna.speed(velocita)
    penna.color(colore)
    for _ in range(numero_lati):
        penna.forward(lunghezza)
        penna.left(angolo)


#Passa le altre funzioni alla funzione disegna_poligono. Permettendo di scegliere la lunghezza e n_lati, colore e velocita
v= chiedi_velocita()
c = chiedi_colore()
n = chiedi_lati()
l=chiedi_lunghezza()
disegna_poligono(n, pen, l, c, v)