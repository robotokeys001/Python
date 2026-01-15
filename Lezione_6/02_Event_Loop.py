#turtle gestisce un ciclo interno che :
    #attende eventi
    #chiama i nostri gestori
    #aggiorna la finestra


import turtle as t

s = t.Screen()

#Abilita l'ascolto della tastiera
s.listen()

#Funzioni di callback frecce tastiera

#Callback funzione go_left
def go_left():
    print("freccia sinistra")

#Callback funzione go_right
def go_right():
    print("freccia destra")

#Callback funzione go_up
def go_up():
    print("freccia su")

#Callback funzione go_down
def go_down():
    print("freccia giù")


#Registro le funzioni callback dell'evento "Tasto premuto"

s.onkey(go_left, "Left")

s.onkey(go_right, "Right")

s.onkey(go_up, "Up")

s.onkey(go_down, "Down")

t.done()

