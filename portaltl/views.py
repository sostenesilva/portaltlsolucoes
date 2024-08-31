from django.shortcuts import render

def index(request):
    return render(request, 'portal/index.html')

def contato(request):
    return render(request, 'portal/contato.html')
