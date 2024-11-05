
def comprimi_stringa(stringa):
    compressa = ""
    contatore = 1
    
    for i in range(1, len(stringa)):
        if stringa[i] == stringa[i - 1]:
            contatore += 1
        else:
            compressa += stringa[i - 1] + str(contatore)
            contatore = 1
    
    
    compressa += stringa[-1] + str(contatore)
    
    if compressa < stringa:
        return compressa
    else:
        return stringa 


while True:
    stringa = input("Inserisci una parola: ")
    print(comprimi_stringa(stringa))
