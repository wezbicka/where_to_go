from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]
    fields = ('file', 'get_preview', 'order_number')
    
    def get_preview(self, obj):
        if not obj.file:
            return format_html(
                "Здесь будет превью, когда вы загрузите файл."
            )
        return format_html(
            '<img src="{}" style="max-height: 200px; max-width: 200px;" >',
            obj.file.url
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
