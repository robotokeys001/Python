#Create un dizionario per le sole lettere senza caratteri speciali e ignorando maiuscole e minuscole

testo='''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!'''

#Rendo il testo in minuscolo
testo= testo.lower()

#Creo un dizionario vuoto
dizionario={}

#Controllo ogni carattere del testo

for carattere in testo:
    #Controllo che il carattere sia una lettera
    if carattere.isalpha():
        #Rendo le lettere minuscola
        lettera= carattere
        #Controllo che la lettera non sia già presente nel mio dizionario
        if lettera not in dizionario.keys():
            #Conto quante volte trovo la lettera nel testo
            occorenze = testo.count(lettera)
            #Creo una copia chiave-valore nel mio dizionario
            dizionario[lettera] = occorenze

print(dizionario)