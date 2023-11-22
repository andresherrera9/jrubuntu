from django.db import models



class entidad_opcion(models.Model):
    entidad = models.CharField(max_length=120)
    opcion = models.CharField(max_length=120) 
    
    def __str__(self):
        return self.opcion
