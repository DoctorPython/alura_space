from django.contrib import admin

from galeria.models import Fotografia

# Register your models here.

class ListantoFotografias(admin.ModelAdmin):

    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome", "legenda")



admin.site.register(Fotografia,ListantoFotografias)
 