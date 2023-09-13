from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, \
    SortableTabularInline, SortableAdminMixin

from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ["get_preview"]
    fields = ('file', 'get_preview', 'order_number')
    
    def get_preview(self, image):
        if not image.file:
            return format_html(
                "Здесь будет превью, когда вы загрузите файл."
            )
        return format_html(
            '<img src="{}" style="max-height: 200px; max-width: 200px;" >',
            image.file.url
        )

    get_preview.short_description = "Превью"
    

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ["title", ]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ("place",)
    list_filter = ("place",)
