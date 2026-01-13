#Scrivere al contrario il terzo verso

testo='''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!'''

#Creo una lista di versi

versi=testo.split('\n')

#Estrapolo il terzo verso

terzo_verso= versi[2]

#terzo_verso[::-1] indica di prendere la lista e estraporale dall'inizio alla fine della stringa ogni lettera contando da -1

print(f'Il terzo verso al contrario : \n{terzo_verso[::-1]}')