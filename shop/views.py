from django.shortcuts import render
from django.views import View
from goods.models import Goods
from orders.models import Orders
from user.models import User
import uuid
import datetime


# Create your views here.

class Index(View):

    def get(self, request):
        goods_list = Goods.objects.all()
        return render(request, 'index.html', {'goods_list': goods_list})


class Detail(View):

    def get(self, request):
        good_id = request.GET.get('good_id')
        good = Goods.objects.get(id=good_id)
        return render(request, 'detail.html', {'good': good})


class ShopCart(View):

    def get(self, request):
        user_id = request.session['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            order_list = user.orders_set.get(status=0)
            return render(request, 'shop_cart.html', {'order_list': order_list})
        else:
            return render(request, 'login.html')

    def post(self, request):
        user_id = request.session['user_id']
        goods_id = request.POST.get('goods_id')
        goods_num = request.POST.get('goods_num')
        order = Orders()
        order.order_id = uuid.uuid4().hex
        order.time = datetime.datetime.now()
        order.goods_num = goods_num
        order.goods = Goods.objects.get(id=goods_id).name
        order.user = User.objects.get(id=user_id).name
        order.price = Goods.objects.get(id=goods_id).price * goods_num


class AddCart(View):

    def post(self, request):
        user_id = request.session['user_id']
        if user_id:
            goods_id = request.POST.get('goods_id')
            goods_num = request.POST.get('goods_num')
            order = Orders()
            order.order_id = uuid.uuid4().hex
            order.time = datetime.datetime.now()
            order.goods_num = goods_num
            order.goods = Goods.objects.get(id=goods_id).name
            order.user = User.objects.get(id=user_id).name
            order.price = Goods.objects.get(id=goods_id).price * goods_num
        else:
            return render(request, 'login.html')


class OrderList(View):

    def get(self, request):
        user_id = request.session['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            order_list = user.orders_set.get(status=1)
            return render(request, 'shop_cart.html', {'order_list': order_list})
        else:
            return render(request, 'login.html')
