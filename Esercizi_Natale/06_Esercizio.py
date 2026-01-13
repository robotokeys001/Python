#Individua l'indice del verso che contiene la parola 'selva'

testo='''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!'''


#Divido il testo in versi
#splitlines() crea una lista dividendo la stringa sui caratteri \n
versi = testo.splitlines()

#ciclo ogni elemento della lista dei versi
for verso in versi:
    #Cerco se esiste la sottostringa 'selva' nel mio verso
    trova= verso.find('selva')
    #Se trovo la sottostringa 'trova' saà diverso da -1
    if trova !=-1:
        #Trovo l'indice del verso all'interno della lista dei versi con index
        #indice = lista.index(elemento)
        print(f'Trovata selva al verso {versi.index(verso)}')

#Altro modo per trovare l'indice del verso

for n in range(len(versi)):
    verso= versi[n]
    #...operazioni per cercare 'selva'
    print(f'''trovata selva all'indice {n}''')