# Generated by Django 2.0 on 2020-04-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=100, verbose_name='联系地址')),
                ('message', models.TextField(verbose_name='留言信息')),
            ],
            options={
                'verbose_name': '留言信息',
                'verbose_name_plural': '留言信息',
            },
        ),
    ]
