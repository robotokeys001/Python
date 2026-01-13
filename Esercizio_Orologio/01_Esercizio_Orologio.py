#TODO
#Utilizando funzioni e loop, disegna un orologio
import turtle
t= turtle.Turtle()

t.home()
#Raggio della circonferenza
raggio=100
#Numero di rettangoli da disegnare
ore=12
#distanza in gradi tra i rettangoli
deg= 360/ore

altezza=20

window = turtle.Screen()
window.bgcolor("yellow")


def draw_rect(t, altezza, larghezza):
    """
    Creo un rettangolo di dimensioni 
    
    """
    t.fillcolor("orange")


    t.forward(larghezza)
    t.right(90)
    t.forward(altezza)
    t.left(-90)
    t.forward(larghezza)
    t.right(90)
    t.forward(altezza)
    t.right(90)
    
    t.end_fill()

#Disegna 12 rettangoli in senso antiorario 
#Da centrare!!!

for _ in range(ore):
    
    t.up()
    t.forward(raggio)
    
    
    
    t.down()
    draw_rect(t, 20,40)

    t.up()
    t.goto(0,0)
    t.left(deg)

    





turtle.done()
    
    


