eta=int(input('Inserisci la tua eta: '))

if eta>=18:
    print('Puoi guidare')
else:
     print('Non puoi guidare')

# TODO:
# Leggi da input una password
# Se la password e "Phyton" stampa accesso consentito
# Altrimenti stampa errore

psw= input('Inserisci password: ').strip()

psw_corretta='Python'
#Operatori logici 'not' 'or' 'and'
if not psw==psw_corretta.strip():
     print('Accesso negato')
else: 
     print('Accesso consentito')
