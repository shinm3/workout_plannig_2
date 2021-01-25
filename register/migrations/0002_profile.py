# Generated by Django 3.0.7 on 2020-06-29 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ハンドルネーム')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='電話番号')),
                ('gender', models.CharField(choices=[('1', '女性'), ('2', '男性')], max_length=2, verbose_name='性別')),
                ('birthday', models.DateField(verbose_name='生年月日')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
