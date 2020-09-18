from django.contrib import admin
from django.http import HttpResponseRedirect
# import copy

# Register your models here.
from .models import Brand, Location_geo, Location_eng, Location_rus, Paints_Oil_Color, Paints_Acrylic_Color, Paints_Gouache_Color, Paints_Water_Color, Paints_Other_Color, \
    Pastels_Oil_Color, Pastels_Soft_Color, Pastels_Water_Color, Pastels_Dry_Color,  Pencils_Colors, Canvas_Choices, Board_Thickness_Choices, Water_Color_Sheet_Size_Choices,\
    Product, Paint_Oil_Color_Product, Paint_Acrylic_Color_Product,\
    Paint_Gouache_Color_Product, Paint_Water_Color_Product, Paint_Other_Color_Product, Pastel_Oil_Color_Product, Pastel_Soft_Color_Product, Pastel_Water_Color_Product,\
    Pastel_Dry_Color_Product, Pencil, Accessories_Molbert, Accessories_Auxiliary_Fluids, Accessories_Palette, Accessories_Mastehin, Canvas_rectangle_frame, Canvas_circular_frame,\
    Canvas_with_rectangle_frame, Canvas_with_circular_frame, Drawing_canvas, Tree_drawing_board, Water_color_sheet, Canvas_with_carton


# def duplicate_event(modeladmin, request, queryset):
#     for object in queryset:
#         object.id = None
#         object.save()
# duplicate_event.short_description = "Duplicate selected record"

def duplicate_event(modeladmin, request, queryset):
    pass

class Dublicate(admin.ModelAdmin):
    actions = [duplicate_event]




admin.site.register(Brand)

admin.site.register(Location_geo)
admin.site.register(Location_eng)
admin.site.register(Location_rus)


admin.site.register(Paints_Oil_Color)
admin.site.register(Paints_Acrylic_Color)
admin.site.register(Paints_Gouache_Color)
admin.site.register(Paints_Water_Color)
admin.site.register(Paints_Other_Color)


admin.site.register(Pastels_Oil_Color)
admin.site.register(Pastels_Soft_Color)
admin.site.register(Pastels_Water_Color)
admin.site.register(Pastels_Dry_Color)


admin.site.register(Pencils_Colors)


admin.site.register(Canvas_Choices)
admin.site.register(Board_Thickness_Choices)
admin.site.register(Water_Color_Sheet_Size_Choices)
# admin.site.register(Product)


admin.site.register(Paint_Oil_Color_Product)
admin.site.register(Paint_Acrylic_Color_Product)
admin.site.register(Paint_Gouache_Color_Product)
admin.site.register(Paint_Water_Color_Product)
admin.site.register(Paint_Other_Color_Product)


admin.site.register(Pastel_Oil_Color_Product)
admin.site.register(Pastel_Soft_Color_Product)
admin.site.register(Pastel_Water_Color_Product)
admin.site.register(Pastel_Dry_Color_Product)


admin.site.register(Pencil)


admin.site.register(Accessories_Molbert)
admin.site.register(Accessories_Auxiliary_Fluids)
admin.site.register(Accessories_Palette)
admin.site.register(Accessories_Mastehin)


admin.site.register(Canvas_rectangle_frame)
admin.site.register(Canvas_circular_frame)
admin.site.register(Canvas_with_rectangle_frame)
admin.site.register(Canvas_with_circular_frame)
admin.site.register(Drawing_canvas)
admin.site.register(Tree_drawing_board)
admin.site.register(Water_color_sheet)
admin.site.register(Canvas_with_carton)



# admin.site.register(Collection)
