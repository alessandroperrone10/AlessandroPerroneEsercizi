class Computer:
    def __init__(self):
        self.__processore = "Intel i5"  #Attributo privato


    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore
        print("Ho modificato il processore!")

pc = Computer()
#Accede all'attributo privato tramite il getter
print(pc.get_processore())

#Modifica l'attributo privao tramite il setter
pc.set_processore("Amd Ryzen 5")
print(pc.get_processore())
      
