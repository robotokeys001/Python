import turtle as t

s= t.Screen()

#Abilito l'ascolto della tastiera
s.listen()

#Dizionario
dirs={
    "LEFT" : (-1,0), #->sinistra
    "RIGHT" : (1,0), #->destra
    "UP" : (0,1), #->su
    "DOWN" : (0,-1) #->giù
}

#Variabile di stato per memorizzare la direzione corrente
direction = dirs['RIGHT']

#Funzione per determinare se la direzione è opposta
# a e b sono due direzioni (x, y)
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

#Esempi di operazioni logiche
"""
a[0] = -1
b[0] = 0

a[0] == -b[0] => -1 == -0 ? --> false

a[1]= 0
b[1] = 1

a[1] == -b[1] => 0 == -1 ? --> false
"""


"""
a[0] = 0
b[0] = 0

a[0] == -b[0] => 0 == -0 ? --> true

a[1]= 0
b[1] = 1

a[1] == -b[1] => 1 == 1 ? --> true
"""

t.done()