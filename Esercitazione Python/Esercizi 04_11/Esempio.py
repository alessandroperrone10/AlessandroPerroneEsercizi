class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False  
        self.menu = {}  

    def descrivi_ristorante(self):
        print("Il ristorante ",self.nome," offre cucina ",self.tipo_cucina,".")

    def stato_apertura(self):
        if self.aperto == True:
            print("Il ristorante ", self.nome, "è aperto")
        else:
            print("Il ristorante ",self.nome , "è chiuso")
        

    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante ",self.nome," è ora aperto.")

    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante ",self.nome," è ora chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print("Piatto ",piatto," aggiunto al menu con prezzo ",prezzo,"€.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            self.menu.pop(piatto)
            print("Piatto",piatto," rimosso dal menu.")
        else:
            print("Il piatto ",piatto," non è nel menu.")

    def stampa_menu(self):
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            print("Menu:")
            for piatto, prezzo in self.menu.items():
                print(piatto,":",prezzo)


class GestioneRistorante:
    def __init__(self):
        self.ristoranti = {}  # Dizionario per memorizzare i ristoranti

    def aggiungi_ristorante(self, nome, tipo_cucina):
        ristorante = Ristorante(nome, tipo_cucina)
        self.ristoranti[nome] = ristorante
        print("Ristorante ",nome," aggiunto con successo.")
        

    def mostra_ristoranti(self):
        if not self.ristoranti:
            print("Nessun ristorante disponibile.")
        else:
            print("Ristoranti registrati:")
            for nome, ristorante in self.ristoranti.items():
                if self.aperto == True:
                    stato = "Aperto"
                else:
                    stato = "Chiuso"
                print(nome," Tipo di cucina:" ,ristorante.tipo_cucina, " Stato:",stato)

    def gestisci_ristorante(self, nome):
        if nome in self.ristoranti:
            ristorante = self.ristoranti[nome]
            while True:
                operazione = input("Cosa vuoi fare? (descrivi, apri, chiudi, aggiungi_piatto, togli_piatto, mostra_menu, indietro): ").lower()
                if operazione == "descrivi":
                    ristorante.descrivi_ristorante()
                elif operazione == "apri":
                    ristorante.apri_ristorante()
                elif operazione == "chiudi":
                    ristorante.chiudi_ristorante()
                elif operazione == "aggiungi_piatto":
                    piatto = input("Inserisci il nome del piatto: ")
                    prezzo = float(input("Inserisci il prezzo del piatto: "))
                    ristorante.aggiungi_al_menu(piatto, prezzo)
                elif operazione == "togli_piatto":
                    piatto = input("Inserisci il nome del piatto da rimuovere: ")
                    ristorante.togli_dal_menu(piatto)
                elif operazione == "mostra_menu":
                    ristorante.stampa_menu()
                elif operazione == "indietro":
                    break
                else:
                    print("Comando non riconosciuto. Riprova.")
        else:
            print("Ristorante ",nome," non trovato.")


# Programma principale
gestione = GestioneRistorante()

while True:
    azione = input("Cosa vuoi fare? (crea_ristorante, lista_ristoranti, gestisci_ristorante, esci): ").lower()

    if azione == "crea_ristorante":
        nome = input("Inserisci il nome del ristorante: ")
        tipo_cucina = input("Inserisci il tipo di cucina del ristorante: ")
        gestione.aggiungi_ristorante(nome, tipo_cucina)

    elif azione == "lista_ristoranti":
        gestione.mostra_ristoranti()

    elif azione == "gestisci_ristorante":
        nome = input("Inserisci il nome del ristorante da gestire: ")
        gestione.gestisci_ristorante(nome)

    elif azione == "esci":
        print("Chiusura del programma.")
        break

    else:
        print("Comando non riconosciuto. Riprova.")
