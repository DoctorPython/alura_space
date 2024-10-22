from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from galeria.models import Fotografia


def index(request):
    '''
    dados = {
         1: {"nome":"Nebulosa de Carina",
        "legenda":"webbtelescope.org / NASA / James Webb"},
         2: {"nome":"Galáxia NGC 1079",
        "legenda":"nasa.org / NASA / Hubble"}
    }
    '''
    fotografias = Fotografia.objects.all()

    return render(request, 'galeria/index.html', {"cards": fotografias})





def imagem(request,foto_id): #puxa o objeto que esta salvo no banco de dados
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

# Create your views here.
