from celery import shared_task
import requests

@shared_task
def send_code(phone, v_code):

    url = "https://106.ihuyi.com/webservice/sms.php?method=Submit"
    data = {
        'account': "C35370225",
        'password': "f67e9e1a15887aa9137810cbca5aa9b6",
        'mobile': phone,
        'content': "您的验证码是：{}。请不要把验证码泄露给其他人。".format(v_code),
        'format': "json",
    }
    requests.post(url=url, data=data)