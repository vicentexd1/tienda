from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.tipo
    class Meta:
        db_table = 'db_tipo_producto'        

class Producto(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_producto'    

class Items_Carrito(models.Model):
    codigo_carrito = models.IntegerField()
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to= "items_carrito", null=True)   

    def __str__(self):
        return self.nombre_producto
    class Meta:
        db_table = 'db_carriopro'  


class Usuario(models.Model):
    usuario = models.CharField(max_length=25)
    contraseña = models.CharField(max_length=25)
    correo = models.CharField(max_length=35)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 

    def __str__(self):
        return self.usuario
    class Meta:
        db_table = 'db_usuario'        

class Suscripcion(models.Model):
    suscrito = models.CharField(max_length=25, null=True)


    def __str__(self):
        return self.suscrito

    class Meta:
        db_table = 'db_suscripcion'    

    