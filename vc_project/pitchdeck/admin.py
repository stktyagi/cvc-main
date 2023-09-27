from django.contrib import admin
from .models import PitchDeck


@admin.register(PitchDeck)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'created_on')
    search_fields = ['name', 'company_name']
    ordering = ('-created_on',)
