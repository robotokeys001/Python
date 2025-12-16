#TODO
#Crea un numero segreto (es 7)
#L'utente tenta di indovinare
#Se troppo alto: stampa troppo altro
#Se troppo basso: stampa troppo basso
#Ripeti finche non indovina

segreto=7

while True:
    numero=int(input('Indovina il numero: '))
    if numero>segreto:
        print('Troppo alto')
        print('ʕっ•ᴥ•ʔっ')
    elif numero<segreto:
        print('Troppo basso')
        print('ʕ-ᴥ-ʔ')
    if numero==segreto:
        print('Hai indovinato')
        print('ʕ⁠っ⁠•⁠ᴥ⁠•⁠ʔ⁠っ  ♡')
        break