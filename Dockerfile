FROM python:3.6.9
COPY . /My_Shop
RUN pip install -r /My_Shop/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
#RUN python /My_Shop/manage.py migrate
