
scelta = input("Quale esercizio si vuole svolgere? Premi 1 per numero positivo, 2 per la somma dei numeri pari, 3 per la somma dei numeri dispari: ")
somma_pari = 0
somma_dispari = 0

if scelta == "1":
    while True:

        numero = int(input("Inserisci un numero: "))

        if  numero > 0:
            input("Il numero è positivo")
            break

elif scelta == "2":
    numero_finale = int(input("Inserisci il numero massimo per la somma dei numeri pari: "))
    
    for n in range(1, numero_finale+1, 2):
            somma_pari += n
    print ("La somma dei numeri pari è: ", somma_pari)
