from django.contrib import admin

# Register your models here.

from .models import Personas, Efectivo, DeclaracionRenta, ConfeCamaras, ActosNotariales, Cambiarias, Productos, RegistroROS, SeguridadSocial


class EfectivoAdmin(admin.TabularInline):
    model = Efectivo
    fk_name = 'titular'
   

class ConfeCamarasAdmin(admin.TabularInline):
    model = ConfeCamaras
    fk_name = 'empresa'


class DeclaracionRentaAdmin(admin.TabularInline):
    model = DeclaracionRenta
    fk_name = 'declarante'

class CambiariasAdmin(admin.TabularInline):
    model = Cambiarias
    fk_name = 'personaTransaccion'

class ProductosAdmin(admin.TabularInline):
    model = Productos
    fk_name = 'titularProducto'

class RegistroROSAdmin(admin.TabularInline):
    model = RegistroROS
    fk_name = 'personaPrincipal'

class ActosNotarialesAdmin(admin.TabularInline):
    model = ActosNotariales
    fk_name = 'personaActo'

class SeguridadSocialAdmin(admin.TabularInline):
    model = SeguridadSocial
    fk_name = 'nombreBeneficiario'


class PersonasAdmin(admin.ModelAdmin):
    inlines = [EfectivoAdmin,ConfeCamarasAdmin,DeclaracionRentaAdmin,CambiariasAdmin,ProductosAdmin,RegistroROSAdmin,ActosNotarialesAdmin,SeguridadSocialAdmin]
    model = Personas
    

admin.site.register(Personas)#,PersonasAdmin)
admin.site.register(Efectivo)
admin.site.register(DeclaracionRenta)
admin.site.register(ConfeCamaras)
admin.site.register(ActosNotariales)
admin.site.register(Cambiarias)
admin.site.register(Productos)
admin.site.register(RegistroROS)
admin.site.register(SeguridadSocial)

