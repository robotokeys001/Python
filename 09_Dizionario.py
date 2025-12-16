#Un dizionario memorizza coppie-->valore
persona={
    'nome':'Luca'', Chiara',
    'cognome': 'Furlan' ', Radaelli',
    'età': 25
}

#Accedo
print(persona['nome'])

#Oppure
print(persona.get('nome'))

#Aggiungi/Modifica valori
persona['città']='Milano', 'Corbetta'
persona['età']=30
persona['hobby']='Guardare la vernice che si asciuga', 'Fissare il muro'


#Rimuovi valori
del persona['età']

print(persona)

print(persona.get('hobby'))

#Quando utilizzarli?
#Quando ervono etichette(nome, età, punteggio..)
#Ottimi per rappresentare gli stati

