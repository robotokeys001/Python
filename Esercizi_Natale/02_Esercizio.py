#Contare le parole

testo='''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!'''

#Il commando split senza dichiarazioni del carattere su cui splittare in automatico splitta la stringa in qualsiasi spazio o a capo
print(f'Il testo contiene {len(testo.split())} parole')

#posso utilizzare e contare spazi e \n
conteggio_parole =testo.count(" ")+ testo.count('\n')+1


print(f'Verifica {conteggio_parole}')