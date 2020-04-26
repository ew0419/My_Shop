from celery import shared_task
import requests

@shared_task
def send_code(phone, v_code):

    url = "https://106.ihuyi.com/webservice/sms.php?method=Submit"
    data = {
        'account': "C35370225",
        'password': "4088a49b5b5d52487535d68098430c2e",
        'mobile': phone,
        'content': "您的验证码是：{}。请不要把验证码泄露给其他人。".format(v_code),
        'format': "json",
    }
    requests.post(url=url, data=data)