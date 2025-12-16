#Un dizionario memorizza coppie-->valore
persona={
    'nome':'Luca'', Chiara',
    'età': 25
}

#Accedo
print(persona['nome'])

#Oppure
print(persona.get('nome'))

#Aggiungi/Modifica valori
persona['città']='Milano'
persona['età']=30

#Rimuovi valori
del persona['età']

print(persona)

#Quando utilizzarli?
#Quando ervono etichette(nome, età, punteggio..)
#Ottimi per rappresentare gli stati

