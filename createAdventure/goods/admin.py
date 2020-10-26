from django.contrib import admin

# Register your models here.
from goods.api.models import Item

admin.site.register(Item)