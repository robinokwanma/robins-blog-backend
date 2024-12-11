from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author',)
    search_fields = ('title', 'author',)
    
    
    
admin.site.register(Article, ArticleAdmin)