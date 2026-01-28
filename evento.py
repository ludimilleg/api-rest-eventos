class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    def imprimirInformacoes(self):
        print(f'Nome do evento: {self.nome}')
        print(f'Nome do local: {self.local}')
        print(f'ID: {self.id}')
        print("------------------")

    @staticmethod
    def calcular_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
