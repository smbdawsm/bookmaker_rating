from django.contrib import admin
from .models import Bookmaker

@admin.register(Bookmaker)
class BookmakerAdmin(admin.ModelAdmin):
    list_display = ('url', 'description', 'image', 'name', 'bonus', 'ratio')



