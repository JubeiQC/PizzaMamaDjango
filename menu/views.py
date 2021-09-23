from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.


def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    # pizzas_names_prices = [f"{pizza.nom} : {pizza.prix}$" for pizza in pizzas]
    # pizzas_names_prices_str = ", ".join(pizzas_names_prices)
    # return HttpResponse(f"Les pizzas : {pizzas_names_prices_str}")
    return render(request, 'menu/index.html', {'pizzas': pizzas})
