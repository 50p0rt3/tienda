from django.db import models

# Create your models here.

class Cliente(models.Model):
    #Campos que tendra la tabla Cliente
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50,verbose_name='Dirección ')
    email=models.EmailField(blank=True, null=True,verbose_name='Correo Electronico')
    phone=models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Articulo(models.Model):
    name=models.CharField(max_length=30)
    section=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return  'el nombre es: %s la seccion es: %s y el precio es $%s' %(self.name,self.section,self.price)

class Pedido(models.Model):
    number=models.IntegerField()
    date=models.DateField()
    delivered=models.BooleanField()




