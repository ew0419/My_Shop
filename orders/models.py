from django.db import models
from user.models import User
from goods.models import Goods


# Create your models here.
class Orders(models.Model):
    CATEGORY_MAP = ((0, '未结算'),
                    (1, '已结算'))
    order_id = models.IntegerField()
    goods_num = models.TextField()
    time = models.TimeField()
    price = models.TextField()
    status = models.IntegerField(choices=CATEGORY_MAP, default=0)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
