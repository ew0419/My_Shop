from django.urls import path
from user.views import *

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('sendcode/',SendCode.as_view()),
    path('alterpassword/',AlterPassword.as_view()),
]
