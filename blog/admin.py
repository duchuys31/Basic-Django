from django.contrib import admin

# Register your models here.
from .models import Post, comment

class comment_inline(admin.TabularInline):
    model = comment

class Postadmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [comment_inline]
admin.site.register(Post,Postadmin)
