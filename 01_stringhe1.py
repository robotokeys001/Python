testo ='Hello world'
print(testo)

l= len('il testo inserito è:' + testo)

print('di lunghezza : ', l)
# Sono un commento in una riga
"""
Siamo piu commenti su piu righe
"""


"""f indica una aggiunta di funzioni o metodi o variabili nella stringa"""

print(f'il primo carattere :  {testo[0]}, il secondo: {testo [-1]}')

s='    Ciao Mondo     '

print(s.lower())# trasforma in minuscolo
print(s.upper())# trasforma in maiuscolo
print(s.strip())# rimuove gli spazi a gli estremi
print(len(s))# mi ritorna la lunghezza
print(len(s.strip()))# mi ritorna la lunghezza senza spazi

print(f'trasforma in minuscolo: {s.lower()}, trasforma in maiuscolo: {s.upper()}, rimuove gli spazi: {s.strip()}, mi da la lunghezza:{len(s)}, mi ritorna la lunghezza senza spazi: {len(s.strip())}')

#Altri metodi---------------------------------------

t='ciao come stai oggi?'
#Sostituisce una stringa con un altra
t.replace('ciao', 'hello')
#Controlla se l'elemento c'e restituendo vero o falso
'come' in t
#Conta quante volte appare il singolo carattere
t.count('o')
#Trova il carattere in questione
t.find('s')

s.replace(' ', '')#Tolgo gli spazi
print(f' Sostituisce la parola con una altra: {t.replace('ciao', 'hello')}, Controlla se e vero o falso:  {'come' in t}, conta quante volte appare il carattere: {t.count('o')}, trova il carattere in questione: {t.find('s')}')

#Altri metodi------------------------------------------------

msg= 'Python'
msg[0]#Restituisce il carattere all indice specificato, in questo caso il primo
msg[-1]#Mi restituisce l'ultimo carattere
msg[1:4]#Mi restituisce il carattere partendo dall'indice indicato e anche quello finale indicato

print(f'estituisce il carattere all indice specificato, in questo caso il primo: {msg[0]}, Mi restituisce l ultimo carattere: {msg[-1]}, Mi restituisce il carattere partendo dall indice indicato e anche quello finale indicato:{msg[1:4]}')

#Altri metodi--------------------------------------------------
