from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#L1
def homepage(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }
    return render(request, "homepage.html", context=context)

#L2
def menu(request):
    return HttpResponse("<ol><li>Prima opzione</li><li>Seconda opzione</li><li>Terza opzione</li></ol>")    

#L3
def chisiamo(request):
    return render(request, "chi_siamo.html")

#L4
def variabili(request):
    context= { 'var1': '10','var2': 'ciao', 'var3' : '123 hello world'}
    return render(request, "variabili.html",context)

#L5
def index(request):
    return render(request, "index.html")