from django.contrib import admin

from items.models import Item_Mast
from items.models import Item_Cat_Mast

admin.site.register(Item_Mast)
admin.site.register(Item_Cat_Mast)
