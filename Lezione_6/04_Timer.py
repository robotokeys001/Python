#ontimer(funzione, millisecondi) richiama unanvolta la funzione dopo N ms.
#Per avere un tick periodico, la funzione si richiama da sola:

#def tick():
#   ...logica...
#   s.ontimer(tick, 120) #richiedi il prossimo tick tra 120 ms

#TODO

import turtle as t

#Creo finestra
s= t.Screen()

pen = t.Turtle(visible=False)
pen.penup()

s.title("tick periodico")


def tick():

    #Logica
    #Pulisco lo schermo con pen.clear()
    #Gli indico la direzione con pen.goto(0,0)-->(0,0) per le coordinate
    #pen.write() mi permette di scrivere 
    pen.clear()
    pen.goto(0,0)
    pen.write("tick", align="center", font=("Arial", 15, "normal"))

    #Ricorsione->Ripeto la funzione ogni n millisecondi
    s.ontimer(tick, 120)
    
tick()

t.done()