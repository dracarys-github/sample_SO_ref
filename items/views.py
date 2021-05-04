from rest_framework.views import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.settings import api_settings

from items.models import Item_Mast

from items.serializer import Item_Mast_Serializer


class ListData:
    '''
    Class used to generalize GET request
    '''
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)


class CreateData:
    '''
    Class used to generalize POST request
    Inherits ConvertListMixin because dynamically detects if data is list of rows or single row
    and assigns many=True to serializer appropriately
    '''
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class Item_Mast_ListView(ListData,CreateData,GenericAPIView):
    queryset = Item_Mast.objects.all().select_related("item_cat_mast")
    serializer_class = Item_Mast_Serializer
