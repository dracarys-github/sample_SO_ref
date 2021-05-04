from rest_framework import serializers

from items.models import Item_Mast
from items.models import Item_Cat_Mast

class IdNameField(serializers.RelatedField):
    def __init__(self, *args, **kwargs):
        id_field = kwargs.pop('id_field', None)
        name_field = kwargs.pop('name_field', None)
        
        super(IdNameField, self).__init__(*args, **kwargs)
        self.id_field = id_field
        self.name_field = name_field        

    def to_representation(self, obj):
        return {
            'id': getattr(obj,self.id_field),
            'name': getattr(obj,self.name_field),
        }

    def to_internal_value(self, data):
        try:
            if(type(data) == dict):
                try:
                    return self.get_queryset().get(**{self.id_field:data["id"]})
                except KeyError:
                    raise serializers.ValidationError('id is a required field.')
                except ValueError:
                    raise serializers.ValidationError('id must be an integer.')
            else: 
                return self.get_queryset().get(**{self.id_field:data})
        except:
            raise serializers.ValidationError('Obj does not exist.')


class Item_Mast_Serializer(serializers.ModelSerializer):
    item_cat_mast = IdNameField(id_field='item_cat_id',name_field='item_cat_name', queryset=Item_Cat_Mast.objects.all())
    class Meta:
        model = Item_Mast
        fields = '__all__'



class Item_Cat_Mast_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Cat_Mast
        fields = '__all__'