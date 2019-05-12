from django.contrib import admin
from .models import Quote, Category

# Custom Admin display
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote', 'is_published', 'author', 'publish_date')
    list_display_links = ('id', 'quote')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('qute', 'author')

# Register your models here.
admin.site.register(Category)
admin.site.register(Quote, QuoteAdmin)