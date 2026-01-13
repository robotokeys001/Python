#Crea un dizionario con ogni carattere del testo con tutte le occorrenze

testo='''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!'''

#Creo un dizionario vuoto
dizionario={}

#Controllo ogni lettera del testo
#E la inserisco nel dizionario vuoto 
for lettera in testo:
    #Se la lettera non compare nelle chiavi del dizionario
    #La funzione .keys() restituisce la lista delle chiavi in un dizionario
    if lettera not in dizionario.keys():
        #Conto quante volto trovo la lettera (carattere) nel testo
        occorrenze = testo.count(lettera)
        #Creo una copia chiave-valore nel mio dizionario
        dizionario[lettera] = occorrenze

print(dizionario)