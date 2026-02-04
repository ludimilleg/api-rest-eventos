from datetime import date
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from agenda.models import Evento
from django.urls import reverse
# Create your views here.
def listar_eventos(request):
    #buscar por um evento 
    eventos = Evento.objects.filter(data__gte=date.today())
    #exibir toda a lista de eventos
    return render(
        request=request, 
        context={"eventos":eventos}, 
        template_name="agenda/listar_eventos.html"
        )

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(
        request=request, 
        context={"evento":evento}, 
        template_name="agenda/exibir_evento.html"
        )

def participar(request):
    eventos_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=eventos_id)
    evento.participantes += 1
    evento.save()

    return HttpResponseRedirect(reverse('exibir_evento', args=(evento.id,)))