# Generated by Django 3.0.7 on 2020-08-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discipline', '0003_auto_20200828_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='remarks',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='備考'),
        ),
    ]
