from django.contrib import admin


from .models import *


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','precio','stock','tipo','imagen','created_at','updated_at']
    search_fields =['codigo','nombre']
    list_per_page = 10
    
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','contraseña','correo','created_at','updated_at']
    



admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Suscripcion)
admin.site.register(Items_Carrito)

