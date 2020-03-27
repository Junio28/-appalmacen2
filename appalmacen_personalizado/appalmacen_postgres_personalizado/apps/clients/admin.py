from django.contrib import admin

# Register your models here.

from apps.clients.models import Client

class ClientAdmin(admin.ModelAdmin):
    #readonly_fields = ('created', 'updated') #No permite edicion de create y update
    list_display = ('name', 'lastname', 'rut', 'address', 'phone')
    ordering =  ('name', 'lastname', 'rut', 'address', 'phone') # En caso que sea una sola ordering('column',)
    #form de busqueda
    search_fields = ('name', 'lastname', 'rut', 'address', 'phone') #Campo relacionado
    #date_hierarchy = 'create'    #campo de fechas
    #list_filter = ('product_types__name',) # Campos relacionados

#     """
#     Para campos many to many
#     def sale_products(self, obj):
#         return ". ".join([c.name for c in obj.products.all().order_by("name")]) 
    
#     sale_products.short_description = "Productos"
  #  """

admin.site.register(Client,ClientAdmin)
