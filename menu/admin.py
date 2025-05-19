from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('indented_title', 'menu', 'parent', 'url', 'is_named_url', 'get_absolute_url_display')
    list_filter = ('menu', 'is_named_url')
    search_fields = ('title', 'url')
    ordering = ('menu', 'parent__id', 'title')
    readonly_fields = ('get_absolute_url_display',)

    def indented_title(self, obj):
        prefix = "—" * obj.get_level()
        return f"{prefix} {obj.title}" if prefix else obj.title
    indented_title.short_description = 'Название'

    def get_absolute_url_display(self, obj):
        return obj.get_absolute_url()
    get_absolute_url_display.short_description = 'Итоговый URL'
