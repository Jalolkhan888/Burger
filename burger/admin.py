from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Chef)
admin.site.register(Client)
admin.site.register(BlogFood)
admin.site.register(Comments)

