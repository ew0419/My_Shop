from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Index.as_view()),
    path('detail/', Detail.as_view()),
    path('shopcart/', ShopCart.as_view()),

]