from http.server import HTTPServer, BaseHTTPRequestHandler
from eventoOnline import Evento_online
from evento import Evento
import json

ev_online1 = Evento_online("Aula de Python")
ev_online2 = Evento_online("Aula de Java")
ev = Evento("Aula presencial", "Rio de Janeiro")
eventos = [ev_online1, ev_online2, ev]

class simpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            data = f"""
            <html>
                <head>
                    <title>Olá, Mundo!</title>
                </head>
                <body>
                    <p>Testando o meu servirdor<p>     
                </body>
            </html>""".encode()
            self.wfile.write(data)
        elif self.path == '/eventos':
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            stylesheet = """
            <style>
                table {
                    border-collapse: collapse;
                }
                td, th {
                    border: 1px solid #ddd;
                    text-align: left;
                    padding: 8px;
                }
            </style>
            """
            
            eventos_html = ""
            for ev in eventos:
                eventos_html += f"""
                <tr>
                    <th>{ev.id}</th>
                    <th>{ev.nome}</th>
                    <th>{ev.local}</th>
                </tr>
                """
            
            data = f"""
            <html>
            <head>{stylesheet}</head>
                <table>
                    <tr>
                        <th>Id</th>
                        <th>Nome</th>
                        <th>Local</th>
                    </tr>
                {eventos_html}
                </table>
            </html>""".encode()
            self.wfile.write(data)

        elif self.path == '/api/eventos': #api rest que está retornando um aplication json
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            list_dict_eventos = []

            for ev in eventos:
                list_dict_eventos.append({
                    'id': ev.id,
                    'Nome': ev.nome,
                    'Local': ev.local})
                
            data = json.dumps(list_dict_eventos).encode()
            self.wfile.write(data)

server = HTTPServer(('localhost', 8888), simpleHandler) #Criação do servidor
server.serve_forever() 