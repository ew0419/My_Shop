# Generated by Django 2.1.8 on 2020-04-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('num', models.IntegerField()),
            ],
        ),
    ]
