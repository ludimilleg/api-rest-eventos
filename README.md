# VamosMarcar

Sistema web desenvolvido em **Django** para listagem e participação em eventos.
O projeto permite visualizar eventos futuros, acessar detalhes de cada evento e registrar a participação, atualizando automaticamente a quantidade de participantes.

## Funcionalidades
- Listagem de eventos com data futura
- Visualização de detalhes do evento
- Participação em eventos
- Contador de participantes
- Organização por categorias

## Tecnologias utilizadas

- Python 3
- Django
- HTML
- CSS básico
- SQLite (banco padrão do Django)

## Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/vamosmarcar-django.git

2.Entre na pasta do projeto:
  cd vamosmarcar-django

3. Crie e ative o ambiente virtual:
  python -m venv venv
  venv\Scripts\activate

4. Instale as dependências:
  pip install django

5. Execute as migrações:
  python manage.py migrate

6. Inicie o servidor:
  python manage.py runserver

7. Acesse no navegador:
  http://127.0.0.1:8000/
