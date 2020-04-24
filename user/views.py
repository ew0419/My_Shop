import redis
import random
from .models import User
from .tasks import send_code
from django.views import View
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password


# Create your views here.
class Register(View):

    def get(self, request):
        fail_status = request.GET.get('fail_status', False)
        return render(request, 'login.html', {'text': '注册', 'url': '/user/register/', 'fail_status': fail_status})

    def post(self, request):
        name = request.POST.get('name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        v_code = request.POST.get('code')
        r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)
        check_code = r.get(phone)
        if v_code != check_code:
            return redirect('/user/register/?fail_status=1')

        phone_check = User.objects.filter(phone=phone)
        if phone_check.exists():
            return redirect('/user/login/?fail_status=2')
        user = User()
        user.name = name
        user.password = password
        user.phone = phone
        user.save()
        return render(request, 'login.html', {'text': '登录', 'url': '/user/login/'})


class Login(View):

    def get(self, request):
        fail_status = request.GET.get('fail_status', False)
        return render(request, 'login.html', {'text': '登录', 'url': '/user/login/', 'fail_status': fail_status})

    def post(self, request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = User.objects.filter(phone=phone)
        if not user.exists:
            return JsonResponse({'msg': '用户不存在'})

        if not check_password(password, user.first().password):
            return JsonResponse({'msg': '密码错误'})
        request.session['user_id'] = user.first().id
        return redirect('/shop/index/')


class SendCode(View):

    def post(self, request):
        phone = request.POST.get('phone')
        v_code = random.randrange(1000, 9999)
        send_code.delay(phone, v_code)

        r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)
        r.set(phone, v_code)
        r.expire(phone, 3000)
        return JsonResponse({'msg': '发送成功'})
