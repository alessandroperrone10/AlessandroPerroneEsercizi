
#contatore numeri primi
count_numeri_primi = 0

while True:
    
    numero = int(input("Inserisci un numero: "))

    for counter in range(numero, -1, -1):   
        print(counter)
    if numero%1 == 0 and numero%numero == 0:
        count_numeri_primi += 1
        print("Il numero è primo")
    else:
        print("Il numero non è primo")
    #print(count_numeri_primi)
    if count_numeri_primi == 5:
        break
    riprovare = input("Vuoi inserire un altro numero? Si o no:  ").lower()
    if riprovare != 'si' or count_numeri_primi == 5:
        break




