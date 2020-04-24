from django.contrib import admin
from django.urls import path
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),

]
