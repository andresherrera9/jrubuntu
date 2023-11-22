from django.db import models



class textros(models.Model):
    texto = models.TextField()
    anexo = models.TextField()
    
    def __str__(self):
        return self.texto

class PostRos(models.Model):
    title = models.TextField()
    image = models.FileField(upload_to="staticfiles/", blank=True)
    image2 = models.FileField(upload_to="static/", blank=True)

    def __str__(self):
        return self.title