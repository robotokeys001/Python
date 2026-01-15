

import turtle as t

#Creo una finestra di turtle
s = t.Screen()

#Do un nome alla finestra
s.title('SNAKE')

#blocco il display automatico dell'animazione
s.tracer(0)

#Abilito l'ascolto della tastiera
s.listen()

#Creo la penna che esegue la renderizzazione dello snake
pen = t.Turtle(visible=False)
pen.speed(0)
pen.penup()


dirs={
    "LEFT" : (-1,0), #->sinistra
    "RIGHT" : (1,0), #->destra
    "UP" : (0,1), #->su
    "DOWN" : (0,-1) #->giù
}
     
# Rappresento la finestra che conterra il gioco
#
# CELL: dimensione di ogni cella (30 pixel)
# GRID: numero di righe/colonne della griglia (20x20)
# WIDTH/HEIGHT: dimensione totale della finestra (600x600 pixel)
CELL=30
GRID=20
WIDTH= HEIGHT = GRID * CELL

#Dimensione del quadrato del serpente
size=CELL-2

#Dico al programma òe dimensioni della finestra
s.setup(WIDTH, HEIGHT)

#---------------------------------------definiamo lo stato dello snake-------------------------------------------------------------------

#Il nostro serpente è rappreesentato da una lista di tuple (x,y)
snake=[(4,10), (5,10), (6,10)]
direction = dirs["RIGHT"]


#--------------------------------------LOGICA DEL PROGRAMMA----------------------------------------------------------------------------------------

def opposti(a, b):

    #Controllo per ogni asse se la direzione è inversa
    x = a[0] == -b[0]# vero se a è uguale a -b
    y = a[1] == -b[1]

    #Restituisco true solo se le x e y sono vere
    return x and y


#Imposto la direzione
def set_dir(newdir):
    #Guardo la direzione attuale dello snake
    global direction

    #Controllo se sono opposti
    op = opposti(direction, newdir)

    #Se sono opposti
    if op:
        print("Ignoro il comando")

    #Se non sono opposti
    else:
        direction = newdir
        print(f"Nuova direzione {newdir}")


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
    
    #Center è una tupla, divido la tupla in due variabili
    x_centro, y_centro= center
    pen.up()
    pen.goto(x_centro - size/2, y_centro - size/2)
    pen.down()
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

#Disegno serpente
def draw_snake(s):
    for cell in s:
        center = to_xy(cell)
        draw_cell(center, size)

def move_snake(snake, direction):
    #Muovo il mio serpente seguendo la direzione, direction
    #(1,0)->destra
    #(-1,0)->sinistra
    #(0,1)->su
    #(0,-1)->giù

    #Estrapolo i vettori di movimento
    dx, dy= direction

    #Estrapolo la posizione della testa
    head_x, head_y= snake[0]

    #Calcolo la posizione della nuova testa
    new_head= (head_x + dx, head_y + dy)

    #Creo il nuovo snake
    new_snake = [new_head] + snake[:-1]
    return new_snake

def tick():
    #Creo uno snake globale
    #Senza global, Python creerebbe una nuova variabile locale. 
    #Qui invece modifichiamo il serpente globale che persiste tra le chiamate.
    global snake

    #Calcolo la NUOVA posizione del serpente
    # move_snake() prende il serpente attuale e la direzione corrente, 
    # restituendo un nuovo serpente spostato di una cella. 
    # Non modifica ancora nulla, solo calcola.
    start_snake=move_snake(snake,direction)

    #Pulisco lo schermo con pen.clear() per cancellare il serpente vecchio
    #Creando la senzazione di movimento
    pen.clear()
    
    #Ridisegno il serpente nella nuova direzione dandogli il serpente iniziale, "start_snake"
    draw_snake(start_snake)

    #Aggiorno lo stato globale
    snake = start_snake

    #Ricorsione->Ripeto la funzione ogni n millisecondi
    #Controllo la velocita alla quale il serpente si muove
    #richiamandolo dopo 250ms
    s.ontimer(tick, 250)

"""Visualizzazione del Ciclo
```
tick() chiamata 1
  ↓
muovi → cancella → disegna → aggiorna stato → aspetta 250ms
                                                    ↓
                                              tick() chiamata 2
                                                    ↓
                                    muovi → cancella → disegna → ..."""


#Funzioni handler
#Callback funzione go_left
def go_left():
    set_dir(dirs['LEFT'])

#Callback funzione go_right
def go_right():
    set_dir(dirs['RIGHT'])

#Callback funzione go_up
def go_up():
    set_dir(dirs['UP'])    

#Callback funzione go_down
def go_down():
    set_dir(dirs['DOWN'])

#Associo gli handler ai callback

s.onkey(go_left, "Left")

s.onkey(go_right, "Right")

s.onkey(go_up, "Up")

s.onkey(go_down, "Down")

tick()

t.done()

