from django.db import models

class Item_Cat_Mast(models.Model):
    item_cat_id = models.AutoField(primary_key=True)
    item_cat_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.item_cat_name


class Item_Mast(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_cat_mast = models.ForeignKey("items.Item_Cat_Mast",  on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item_name