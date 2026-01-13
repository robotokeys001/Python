#Contare le righe

testo='''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!'''

#Il metodo count conta quante volte in una stringa compare la serie di caratteri che diamo di input
numero_righe = testo.count('\n')+1


#conto count('\n')+ perche l'ultima riga non contiene un \n
print(f"nel testo ci sono {numero_righe} di righe effettive")