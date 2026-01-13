#Individuate la posizione della stringa 'selva' all'interno del verso

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
    #Se trovo la sottostringa 'trova' sarà diverso da -1
    if trova !=-1:
        #Trova 'selva'
        print(f'la selva si trova nella posizione {trova} del verso')
