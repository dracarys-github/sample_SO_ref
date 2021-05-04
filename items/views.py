from rest_framework.views import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.settings import api_settings

from items.models import Item_Mast

from items.serializer import Item_Mast_Serializer

class Item_Mast_ListView(GenericAPIView):
    queryset = Item_Mast.objects.all().select_related("item_cat_mast")
    serializer_class = Item_Mast_Serializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)