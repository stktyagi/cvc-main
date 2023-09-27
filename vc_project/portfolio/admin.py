from django.contrib import admin
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'image', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_on',)
