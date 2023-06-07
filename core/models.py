from django.db import models

# Create your models here.
class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Gato(models.Model):
    idGato = models.AutoField(primary_key=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    edad = models.IntegerField()
    comentario =models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    file = models.ImageField(upload_to="img/gato")

    def __str__(self):
        return self.nombre

class Perro(models.Model):
    idPerro = models.AutoField(primary_key=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    edad = models.IntegerField()
    comentario =models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    file = models.ImageField(upload_to="img/perro")

    def __str__(self):
        return self.nombre