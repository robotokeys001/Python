
#Ciclo while: ripete l'operazione finche la condizione non diventa falsa 
i=1
while i<=7:
    print(i)
    i+=1

#Altri metodi------------------------------------

parola= input('Scrivi una parola per ripeterla: ')

i=1
while True:
    for i in range(30):
        print(parola)
    if i<=30:
        msg=input('Scrivi: stop, per interompere, o invio per continuare ')
    if msg=='stop':
        print('Hai interrotto il loop')
        break
    else:
        nuova_parola=input('scrivine una altra per ripeterla: ')
        parola=nuova_parola
        for i in range(30):
            print(parola)
    #TODO:
    #Continua a chiedere ad un utente la psw
    #Se l utente scrive la psw corretta: interrompi il ciclo
    #Altrimenti continua a chiedere

psw= input('Inserisci password: ').strip()

psw_corretta='Python'

while True:    
    if psw==psw_corretta.strip():
        print('Password Corretta')
        break
    else:
        psw=input('Password errata, ritenta: ')

