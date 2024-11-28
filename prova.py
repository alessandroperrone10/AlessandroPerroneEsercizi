class Ristoramte:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}

    def descrizione_ristorante(self):
        print(f"Il ristorante:{self.nome} ,offre cucina:  {self.tipo_cucina} .")
        if self.aperto == False:
            print("Attualmente il ristorante è chiuso, riprova a passare più tardi.")
        else:
            print("Il ristorante è aperto. Benvenuti!")

    def stato_apertura(self):
        if self.aperto == False:
            print("Attualmente il ristorante è chiuso, riprova a passare più tardi.")
        else:
            print("Il ristorante è aperto. Benvenuti!")
    
    def apri_ristorante(self):
        self.aperto = True
        print("Hai aperto il ristorante")

    def chiudi_ristorante(self):
        self.aperto = False
        print("Hai chiuso il ristorante")
    
    def aggiungi_al_menu(self):
        nome_piatto = input("Inserisci il nome del piatto")
        prezzo = float(input("Inserisci il prezzo del piatto: ", nome_piatto))

        self.menu[nome_piatto] = prezzo
        print(f"Hai aggiunto il piatto {nome_piatto} al menu con prezzo {prezzo}.")

    def togli_dal_menu(self):
        print(self.menu)
        nome_piatto = input("Inserisi il nome del piatto che vuoi eliminare: ").lower()
        if nome_piatto in self.menu[nome_piatto].lower():
            self.menu.pop(nome_piatto)
            print(f"Hai rimosso il piatto {nome_piatto} dal menu.")
        else:
            print("Hai inserito un piatto che non è presente nel menù.")

    def stampa_menu(self):
        print("Menu del ristorante:")
        for piatto, prezzo in self.menu.items():
            print(f"{piatto}: {prezzo}���")




