# Generated by Django 3.0.7 on 2020-07-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20200702_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('1', '女性'), ('2', '男性')], max_length=2, verbose_name='性別'),
        ),
    ]
