from evento import Evento

class Evento_online(Evento):
    def __init__(self, nome, _=""):
        local = local= f"http://tamarcado.com/evento?id={Evento_online.id}"
        super().__init__(nome, local)

    def imprimirInformacoes(self): 
        print(f'ID: {self.id}')
        print(f'Nome do evento: {self.nome}')
        print(f'link: {self.local}')
        print("------------------")