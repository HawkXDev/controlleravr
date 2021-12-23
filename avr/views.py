from django.shortcuts import render


def index(request):
    return render(request, 'avr/index.html')


def results(request):
    return render(request, 'avr/results.html')
