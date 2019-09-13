from django.contrib import admin
from .models import Board_element

class Board_elementAdmin(admin.ModelAdmin):
    pass



admin.site.register(Board_element, Board_elementAdmin)
