from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    list_display_links = ('name', )
    readonly_fields = ('get_image', )
    search_fields = ('name', 'short_desc', 'full_desc')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="90" height="60"')

    get_image.short_description = 'Изображение'


admin.site.register(Product, ProductAdmin)
