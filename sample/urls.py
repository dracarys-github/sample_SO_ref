from django.urls import path
from items import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("item_mast/", views.Item_Mast_ListView.as_view()),
]