from django.contrib import admin
from .models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']
    ordering = ('-created_on',)
