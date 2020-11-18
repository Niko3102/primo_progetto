from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista
from django.views.generic.detail import DetailView

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage2.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

class ArticoloDetailViewCB(DetailView):
    model = Articolo
    template_name = "articolo_detail.html"