__autor__ = 'ESANTIAGO'

from django.shortcuts import render
from django.http import HttpResponse

class Tarefa(object):
    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data

    def __str__(self):
        return self.titulo

def home(request):
    return HttpResponse("Olá")

def sobre(request):
    return HttpResponse("Ewerton Santiago")

def tarefa(request, ano, mes, dia):
    return HttpResponse("tarefa:" + str(ano) + "/" + str(mes) + "/" + str(dia))