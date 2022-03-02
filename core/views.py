from django.views.generic import View
from django.shortcuts import render

class HomeView(View): # esta clase nos da acceso al pous request y el get request
    def get(self, request, *args, **kwargs): # requestes cuando enviamos informacion al servidor *args y *kwargs
        #hace referencia a cualquier parametro que el objeto del request que estemos llamando pueda tener
        contex={ # esto es un diccionario

        }
        return render(request, 'index.html', contex) # las dos comillas significa el template, osea, nuestro html que vamos a mostrar
