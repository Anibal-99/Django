from django.db import models

# Create your models here.

class Post(models.Model): # se agrega el parametro de model
    # aqui agregamos los campos que queremos crear y hacer que se puedan editar
    title=models.CharField(max_length=250)
    content=models.TextField() # el TextField es igual que el Char solo que mas grande para poder agrgear mas contenido

    def __str__(self):
        return self.title # con esto podemos devolver el nombre del post que creamos en el panel de administracion
