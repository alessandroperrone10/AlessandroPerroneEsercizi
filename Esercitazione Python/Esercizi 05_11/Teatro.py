class Posto:
    def __init__(self,__numero,__fila,__occupato):
        self.__numero = 0
        self.__fila = " "
        self.__occupato = False

    def get_numero(self):
        pass

    def set_numero(self):
        pass

    def get_fila(self):
        pass

    def set_fila(self):
        pass

    def get_occupato(self):
        pass

    def prenota():
        pass

    def libera():
        pass

class PostoVIP(Posto):
    def __init__(self, __numero, __fila, __occupato,servizi_extra):
        super().__init__(__numero, __fila, __occupato)
        self.servizi_extra = servizi_extra

class PostoStandard(Posto):
    pass


class Teatro:
    def __init__(self):
        __posti = {}

    def stampa_posti_occupati():
        pass

    def prenota_posto():
        pass