from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.

def index(request):
   ''' pizzas = Pizza.objects.all()

    #pizza_names = [pizza.nom for pizza in pizzas]
    liste_final = []
    # Equivalent de : pizza_name_prix = [pizza.nom +" : "+ pizza.prix + "€" for pizza in pizzas]
    for pizza in pizzas:
        pizza_name_prix = pizza.nom + " : " + str(pizza.prix) + "€"
        liste_final.append(pizza_name_prix)
    pizza_name_prix_str = ", ".join(liste_final)

    return HttpResponse("LES PIZZAS : " + pizza_name_prix_str)'''
   pizzas = Pizza.objects.all().order_by('prix')
   return render(request, 'menu/index.html', {'pizzas' : pizzas})