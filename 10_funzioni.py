#Le funzioni si definiscono con la keyword "def"
#I parametri della funzione servono per passare dei valori dal programma alla funzione
def nome_funzione(parametro_1, parametro_2):
    """
    Docstring for nome_funzione
    
    :param parametro_1: Prende il primo numero
    :param parametro_2: Prende il secondo numero
    """

    #Restituisco i due valori
    #return parametro_1+parametro_2

    #oppure
    #posso metterle all'interno di una variabile
    risultato=parametro_1+parametro_2

    #e restituirla
    return risultato

print(nome_funzione(1,2))

def saluta(nome="Luigi"):
    """
    Docstring for saluta
    
    :param nome: Se nn passo nessun valore alla funzione saluta()
    nome sarà uguale a Luigi o al valore messo di default

    """
    print(f"Ciao {nome}")

saluta('Chiara')

#-------------------------------------------------------------------------------

#TODO
#Definisci una funzione quadrato(x) ---> restituisce quadrato
#Chiama la funzione su 2 valori diversi
#Stampa il risultato

def quadrato(x):
    """
    Docstring for quadrato
    
    Calcolo il quadrato di un valore

    """
    per_se_stesso=x*x
    return per_se_stesso

print(quadrato(10))

def eleva(x,y):
    risultato=1
    for _ in range(y):
        risultato= risultato*x
    return risultato

print(eleva(3,1))

def cubo(x):
    """
    Docstring for cubo
    
    Innesto la funzione eleva() con parametro x, dove metto un valore, e un valore determinato
    """
    return eleva(x,3)

print(cubo(4))

