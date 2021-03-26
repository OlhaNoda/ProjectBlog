from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)

