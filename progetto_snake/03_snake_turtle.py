#TODO(visuale)
#Usa turtle per disegnare due celle affiancate definite da una lista di tuple
#-Config griglia (CELL, GRID, WIDTH, HEIGHT)
#-Funzione to_xy(cell) -> (x,y) in pixel
#-Funzione draw_cell(center, size, outline, fill)
#-Disegna ciascuna cella della lista 'snake'
#
#Suggerimenti
# snake=[(5,10), (6,10)]
# size = CELL-2
# usa s.tracer(0) e poi s.update() per evitare animazione lenta
#
#Scrivi qui tutto il codice turtle

import turtle as t


window= t.Screen()

# Rappresento la finestra che conterra il gioco
#
# CELL: dimensione di ogni cella (30 pixel)
# GRID: numero di righe/colonne della griglia (20x20)
# WIDTH/HEIGHT: dimensione totale della finestra (600x600 pixel)
CELL=30
GRID=20
WIDTH= HEIGHT = GRID * CELL

snake=[(5,10), (6,10)]

size=CELL-2

window.setup(WIDTH, HEIGHT)

#Scopo: Converte coordinate logiche della griglia in coordinate pixel sullo schermo.
#Come funziona:
#
#Riceve una tupla cell tipo (5, 10) che rappresenta colonna e riga nella griglia
# x_c * CELL: posizione pixel dell'angolo sinistro della cella
# + CELL/2: aggiunge metà cella per ottenere il centro
#Esempio: (5, 10) → (165, 315) pixel
def to_xy(cell):
    x_c, y_c= cell

    #Calcolo del centro della cella nel punto x
    x_p= -(WIDTH/2)+(x_c*CELL)+CELL/2

    #Calcolo del centro della cella nel punto y
    y_p= -(HEIGHT/2)+(y_c*CELL)+CELL/2
    return (x_p,y_p)

#Scopo: Disegna un quadrato centrato in una posizione.
#Passaggi:
#
#Crea una nuova tartaruga (pen)
#Si sposta al punto di partenza (angolo in basso a sinistra del quadrato)
#Disegna 4 lati del quadrato ruotando di 90° dopo ogni lato

def draw_cell(center, size):
    pen = t.Turtle()
    x_centro, y_centro= center
    pen.up()
    pen.goto(x_centro - size/2, y_centro - size/2)
    pen.down()
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

for cell in snake:
    center = to_xy(cell)
    draw_cell(center, size)



t.done()

