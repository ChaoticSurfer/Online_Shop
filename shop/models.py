from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, MaxValueValidator, \
    EmailValidator
from datetime import timedelta
from datetime import  datetime as django_datetime
import datetime

# current_date = datetime.datetime.now()


# Create your models here.
class Brand(models.Model):
    brand_id = models.AutoField
    brand_name = models.CharField(max_length=40)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.brand_name


class Location_geo(models.Model):
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.location

class Location_eng(models.Model):
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.location

class Location_rus(models.Model):
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.location

# class Paint(models.Model):
#     paint_id = models.AutoField
#     name = models.CharField(max_length=50)
#     brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)  # .CharField(max_length=40, models)
#     amount_volume = models.CharField(max_length=40)  # REMAINDER UP
#     type_of_product = models.CharField(max_length=50, default=None)
#     image_low_quality = models.ImageField(upload_to="shop/images", default="")
#     image_high_quality = models.ImageField(upload_to="shop/images", default="")
#     price = models.IntegerField()
#     amount_in_warehouse = models.IntegerField(default=None)
#     material = models.CharField(max_length=50,default=None)
#     pub_date = models.DateField(auto_now_add=True)
#
#
#     #
#     def __str__(self):
#         return f'{self.name}, {self.pub_date}'

class Paints_Oil_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Paints_Acrylic_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Paints_Gouache_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Paints_Water_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Paints_Other_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Pastels_Oil_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Pastels_Soft_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Pastels_Water_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Pastels_Dry_Color(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name


class Pencils_Colors(models.Model):
    color_code = models.CharField(max_length=15)
    color_name = models.CharField(max_length=40)

    def __str__(self):
        return self.color_name

class Canvas_Choices(models.Model):
    canvas_choices = models.CharField(max_length=40)

    def __str__(self):
        return self.canvas_choices

class Board_Thickness_Choices(models.Model):
    board_thickness = models.CharField(max_length=40)

    def __str__(self):
        return self.board_thickness

class Water_Color_Sheet_Size_Choices(models.Model):
    sheet_size = models.CharField(max_length=40)

    def __str__(self):
        return self.sheet_size


TYPE_CHOICES = (
    ("საღებავი", "საღებავი"),
    ("პასტელი", "პასტელი"),
    ("ფანქარი", "ფანქარი"),
    ("აქსესუარები", "აქსესუარები"),
    ("სახატავი დაფები", "სახატავი დაფები"),
    ("ჩარჩო პასპარტუ", "ჩარჩო პასპარტუ"),
)
MATERIAL_CHOICES_PAINT = (
    ("OIL COLOR", "OIL COLOR"),
    ("ACRYLIC COLOR", "ACRYLIC COLOR"),
    ("GOUACHE", "GOUACHE"),
    ("WATER COLOR", "WATER COLOR"),
    ("OTHER", "OTHER"),
)
MATERIAL_CHOICES_PASTEL = (
    ("OIL", "OIL"),
    ("SOFT", "SOFT"),
    ("WATER COLOR", "WATER COLOR"),
    ("DRY", "DRY"),
)
MATERIAL_CHOICES_PENCIL = (
    ("GRAFFITI", "GRAFFITI"),
    ("WATER COLOR", "WATER COLOR"),
    ("COAL", "COAL"),
    ("OTHER", "OTHER"),
)
MATERIAL_CHOICES_ACCESSORIES = (
    ("მოლბერტი, ეტიუდნიკი", "მოლბერტი, ეტიუდნიკი"),
    ("დამხმარე სითხეები", "დამხმარე სითხეები"),
    ("პალიტრა", "პალიტრა"),
    ("სამხატვრო შპატელი(მასტეხინი)", "სამხატვრო შპატელი(მასტეხინი)"),
)
MATERIAL_CHOICES_DRAWING_BOARDS = (
    ("ქვეჩარჩო", "ქვეჩარჩო"),
    ("ქვეჩარჩოზე გადაჭიმული ტილო", "ქვეჩარჩოზე გადაჭიმული ტილო"),
    ("სახატავი ტილო", "სახატავი ტილო"),
    ("ხის სახატავი დაფა", "ხის სახატავი დაფა"),
    ("აკვარელის სახატავი ფურცელი", "აკვარელის სახატავი ფურცელი"),

)
MATERIAL_CHOICES_FRAME_PASPARTU = (
    ("ხის", "ხის"),
    ("პლასტმასის", "პლასტმასის"),
    ("ალუმინის", "ალუმინის"),
)
PACK_CHOICES = (
    ("ერთი", "ერთი"),
    ("კოლექცია", "კოლექცია"),
)

# კარგად დასამუშავებელი

# MOON = (
#     ("სავსე მთვარე", "სავსე მთვარე"),
#     ("ცარიელი მთვარე", "ცარიელი მთვარე"),
#     ("ნახევარ მთვარე", "ნახევარ მთვარე"),
#     ("არაფერი", "არაფერი")
# )

THICKNESS_CHOICES = (
    ("20mmX30mm", "20mmX30mm"),
    ("20mmX40mm", "20mmX40mm"),
    ("25mmX50mm", "25mmX50mm")
)

CANVAS_SIZE_CHOICES = (
    ("ზომა1", "ზომა1"),
    ("ზომა2", "ზომა2"),
    ("ზომა3", "ზომა3")
)

OVERLAY_CHOICES_GEO = (
    ("გვერდზე", "გვერდზე"),
    ("უკან", "უკან")
)

OVERLAY_CHOICES_ENG = (
    ("around", "around"),
    ("back", "back")
)

OVERLAY_CHOICES_RUS = (
    ("на странице", "на странице"),
    ("назад", "назад")
)


BOARD_THICKNESS_CHOICES = (
    ("თხელი", "თხელი"),
    ("საშუალო", "საშუალო"),
    ("სქელი", "სქელი")
)

BOARD_SIZE_CHOICES = (
    ("ზომა1", "ზომა1"),
    ("ზომა2", "ზომა2"),
    ("ზომა3", "ზომა3")
)

WATER_COLOR_SHEET_SIZE_CHOICES = (
    ("ზომა1", "ზომა1"),
    ("ზომა2", "ზომა2"),
    ("ზომა3", "ზომა3")
)

TYPE_OF_ART_CHOICES = (
    ("paper", "paper"),
    ("embroidered", "embroidered"),
    ("canvas", "canvas"),
    ("jersey", "jersey")

)


class Product(models.Model):
    product_id = models.AutoField
    product_name_geo = models.CharField(max_length=50, default="")
    product_name_eng = models.CharField(max_length=50, default="")
    product_name_rus = models.CharField(max_length=50, default="")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    description_geo = models.CharField(validators=[MinLengthValidator(40)], max_length=300, default="")
    description_eng = models.CharField(validators=[MinLengthValidator(40)], max_length=300, default="")
    description_rus = models.CharField(validators=[MinLengthValidator(40)], max_length=300, default="")
    image_low_quality = models.ImageField(upload_to="static/media/shop/images", default="")
    image_high_quality = models.ImageField(upload_to="static/media/shop/images", default="")
    price = models.FloatField()
    weight = models.FloatField(default=0)
    amount_in_warehouse = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    location_geo = models.ForeignKey(Location_geo, on_delete=models.SET_NULL, null=True, blank=True)
    location_eng = models.ForeignKey(Location_eng, on_delete=models.SET_NULL, null=True, blank=True)
    location_rus = models.ForeignKey(Location_rus, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    # my_date = pub_date+timedelta(hours=5)
    # new_date = models.DateTimeField(null=True, blank=True)
    # current_date = datetime.datetime.now()

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image_low_quality.url
    #     except:
    #         url = ''
    #     return url

    def __str__(self):
        return self.product_name_geo

# ეს შედის Paint-ში ანუ საღებავებში
class Paint_Oil_Color_Product(Product):
    verbose_name = "Paint"
    sub_verbose_name = "Paint_Oil_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PAINT, default="OIL COLOR")
    color = models.ForeignKey(Paints_Oil_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Paint-ში ანუ საღებავებში
class Paint_Acrylic_Color_Product(Product):
    verbose_name = "Paint"
    sub_verbose_name = "Paint_Acrylic_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PAINT, default="ACRYLIC COLOR")
    color = models.ForeignKey(Paints_Acrylic_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Paint-ში ანუ საღებავებში
class Paint_Gouache_Color_Product(Product):
    verbose_name = "Paint"
    sub_verbose_name = "Paint_Gouache_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PAINT, default="GOUACHE")
    color = models.ForeignKey(Paints_Gouache_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Paint-ში ანუ საღებავებში
class Paint_Water_Color_Product(Product):
    verbose_name = "Paint"
    sub_verbose_name = "Paint_Water_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PAINT, default="WATER COLOR")
    color = models.ForeignKey(Paints_Water_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Paint-ში ანუ საღებავებში
class Paint_Other_Color_Product(Product):
    verbose_name = "Paint"
    sub_verbose_name = "Paint_Other_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PAINT, default="OTHER")
    color = models.ForeignKey(Paints_Other_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Pastel-ში ანუ პასტელებში
class Pastel_Oil_Color_Product(Product):
    verbose_name = "Pastel"
    sub_verbose_name = "Pastel_Oil_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PASTEL, default="OIL")
    color = models.ForeignKey(Pastels_Oil_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Pastel-ში ანუ პასტელებში
class Pastel_Soft_Color_Product(Product):
    verbose_name = "Pastel"
    sub_verbose_name = "Pastel_Soft_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PASTEL, default="SOFT")
    color = models.ForeignKey(Pastels_Soft_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Pastel-ში ანუ პასტელებში
class Pastel_Water_Color_Product(Product):
    verbose_name = "Pastel"
    sub_verbose_name = "Pastel_Water_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PASTEL, default="WATER COLOR")
    color = models.ForeignKey(Pastels_Water_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Pastel-ში ანუ პასტელებში
class Pastel_Dry_Color_Product(Product):
    verbose_name = "Pastel"
    sub_verbose_name = "Pastel_Dry_Color_Product"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PASTEL, default="DRY")
    color = models.ForeignKey(Pastels_Dry_Color, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Pencil-ში ანუ ფანქრებში
class Pencil(Product):
    verbose_name = "Pencil"
    sub_verbose_name = None
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_PENCIL)
    color = models.ForeignKey(Pencils_Colors, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Accessories-ში ანუ აქსესუარებში
class Accessories_Molbert(Product):
    verbose_name = "Accessories"
    sub_verbose_name = "Accessories_Molbert"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, default="")
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Accessories-ში ანუ აქსესუარებში
class Accessories_Auxiliary_Fluids(Product):
    verbose_name = "Accessories"
    sub_verbose_name = "Accessories_Auxiliary_Fluids"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, default="")
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Accessories-ში ანუ აქსესუარებში
class Accessories_Palette(Product):
    verbose_name = "Accessories"
    sub_verbose_name = "Accessories_Palette"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, default="")
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Accessories-ში ანუ აქსესუარებში
class Accessories_Mastehin(Product):
    verbose_name = "Accessories"
    sub_verbose_name = "Accessories_Mastehin"
    amount_volume = models.CharField(max_length=40, default="")
    material = models.CharField(max_length=30, default="")
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Canvas_rectangle_frame(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Canvas_rectangle_frame"
    amount_volume = models.CharField(max_length=40, default="", null=True, blank=True)
    material = models.CharField(max_length=30, default="")
    thickness = models.CharField(max_length=30, choices=THICKNESS_CHOICES, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Canvas_circular_frame(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Canvas_circular_frame"
    amount_volume = models.CharField(max_length=40, default="", null=True, blank=True)
    material = models.CharField(max_length=30, default="")
    pack = "კოლექცია"

    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Canvas_with_rectangle_frame(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Canvas_with_rectangle_frame"
    amount_volume = models.CharField(max_length=40, default="", null=True, blank=True)
    material = models.CharField(max_length=30, default="")
    thickness = models.CharField(max_length=30, choices=THICKNESS_CHOICES, null=True, blank=True)
    canvas_type = models.ForeignKey(Canvas_Choices, on_delete=models.SET_NULL, null=True, blank=True)
    overlay_geo = models.CharField(max_length=30, choices=OVERLAY_CHOICES_GEO, null=True, blank=True)
    overlay_eng = models.CharField(max_length=30, choices=OVERLAY_CHOICES_ENG, null=True, blank=True)
    overlay_rus = models.CharField(max_length=30, choices=OVERLAY_CHOICES_RUS, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Canvas_with_circular_frame(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Canvas_with_circular_frame"
    amount_volume = models.CharField(max_length=40, default="", null=True, blank=True)
    material = models.CharField(max_length=30, default="")
    canvas_type = models.ForeignKey(Canvas_Choices, on_delete=models.SET_NULL, null=True, blank=True)
    overlay_geo = models.CharField(max_length=30, choices=OVERLAY_CHOICES_GEO, null=True, blank=True)
    overlay_eng = models.CharField(max_length=30, choices=OVERLAY_CHOICES_ENG, null=True, blank=True)
    overlay_rus = models.CharField(max_length=30, choices=OVERLAY_CHOICES_RUS, null=True, blank=True)
    pack = "კოლექცია"

    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Drawing_canvas(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Drawing_canvas"
    height = models.CharField(max_length=40, default="")
    drawing_canvas_type = models.ForeignKey(Canvas_Choices, on_delete=models.SET_NULL, null=True, blank=True)
    pack = "ერთი"
    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Tree_drawing_board(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Tree_drawing_board"
    amount_volume = models.CharField(max_length=40, default="", null=True, blank=True)
    thickness = models.ForeignKey(Board_Thickness_Choices, on_delete=models.SET_NULL, null=True, blank=True)
    pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")

    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Water_color_sheet(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Water_color_sheet"
    color = models.CharField(max_length=40, default="")
    size = models.ForeignKey(Water_Color_Sheet_Size_Choices, on_delete=models.SET_NULL, null=True, blank=True)
    pack = "კოლექცია"

    def __str__(self):
        return self.product_name_geo

# ეს შედის Drawing_boards-ში ანუ სახატავი დაფები
class Canvas_with_carton(Product):
    verbose_name = "Drawing_boards"
    sub_verbose_name = "Canvas_with_carton"
    drawing_canvas_type = models.ForeignKey(Canvas_Choices, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=40, default="")
    pack = "კოლექცია"

    def __str__(self):
        return self.product_name_geo

#ამ მოდელში არამგონია sub_verbose_name დაგჭირდეს, MATERIAL_CHOICES_FRAME_PASPARTU ამის მიხედვით გაფილტრე და verbose_name გამოიყენე, მე ასე წარმოვიდგინე
# class Frame_Paspartu(Product):
#     verbose_name = "Frame_Paspartu"
#     sub_verbose_name = None
#     amount_volume = models.CharField(max_length=40, default="")
#     material = models.CharField(max_length=30, choices=MATERIAL_CHOICES_FRAME_PASPARTU, default="")
#     type_of_art = models.CharField(max_length=30, choices=TYPE_OF_ART_CHOICES, default="")
#     paspartu_color = models.CharField(max_length=40, default="", null=True, blank=True)
#     frame_color = models.CharField(max_length=40, default="")
#     paspartu_size = models.CharField(max_length=30, default="", null=True, blank=True)
#     frame_size = models.CharField(max_length=30, default="", null=True, blank=True)
#     pack = models.CharField(max_length=20, choices=PACK_CHOICES, default="ერთი")
#
#     def __str__(self):
#         return self.product_name_geo

