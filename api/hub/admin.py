from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('title',)