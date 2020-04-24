from django.shortcuts import render
from django.views import View
from .models import User
from django.http.response import JsonResponse
from django.contrib.auth.hashers import check_password


# Create your views here.
class Register(View):

    def get(self, request):
        return render(request, 'login.html', {'text':'注册', 'url':'user/register'})

    def post(self, request):
        name = request.POST.get('name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        phone_check = User.objects.filter(phone=phone)
        if not phone_check.exists():
            user = User()
            user.name = name
            user.password = password
            user.phone = phone
            user.save()
        return render(request, 'login.html', {'text':'登录', 'url':'user/login'})



class Login(View):

    def get(self, request):
        return render(request, 'login.html', {'text':'登录', 'url':'user/login'})

    def post(self, request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = User.objects.filter(phone=phone)
        if user.exists:
            if check_password(password, user.first().password):
                request.session['user_id'] = user.first().id

