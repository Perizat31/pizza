from django.contrib import admin 

from .models import *

class menuAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_display_links = ("id","name")
    search_fields = ("name",)

admin.site.register(menu,menuAdmin)

class pizzaAdmin(admin.ModelAdmin):
    list_display = ("id","pizzaname")
    list_display_links = ("id","pizzaname")
    search_fields = ("pizzaname",)
admin.site.register(pizza,pizzaAdmin)

admin.site.register(City)
admin.site.register(Street)
admin.site.register(Address)
admin.site.register(CustomerUser)
admin.site.register(Deliveryuser)
admin.site.register(Orderstatus)
admin.site.register(Order)
admin.site.register(Cardholder)
admin.site.register(Cardtype)
admin.site.register(Card)
admin.site.register(Paymentstatus)
admin.site.register(UserCard)








