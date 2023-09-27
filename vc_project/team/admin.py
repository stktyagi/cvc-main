from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_on', 'image', )
    search_fields = ['name', 'title', 'content']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_on',)
