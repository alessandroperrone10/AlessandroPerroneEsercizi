#Esercizio 2
# Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numeri da n a 0 (compreso), decrementando di 1.
# Deve potersi ripete all’infinito


#Ciclo all'infinito
while True:
  numero = int(input("Inserisci un numero: "))

#Verifico se il numero è maggiore di 0
  if numero < 0:
    print("Il numero è negativo")
  else:

      while numero in range(numero, -1 , -1):
          print(numero)
          numero -= 1