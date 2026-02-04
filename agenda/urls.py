from agenda.views import listar_eventos, exibir_evento, participar
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", listar_eventos, name="listar_eventos"),
    path("eventos/<int:id>/", exibir_evento, name="exibir_evento"),
    path("participar/", participar, name="participar")
]