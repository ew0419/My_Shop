from django.urls import path
from shop.views import *

urlpatterns = [
    path('index/', Index.as_view()),
    path('detail/', Detail.as_view()),
    path('shopcart/', ShopCart.as_view()),
]