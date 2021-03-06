# Generated by Django 3.0.7 on 2020-08-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discipline', '0002_discipline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='weight_1',
            field=models.FloatField(blank=True, null=True, verbose_name='重量1'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_10',
            field=models.FloatField(blank=True, null=True, verbose_name='重量10'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_2',
            field=models.FloatField(blank=True, null=True, verbose_name='重量2'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_3',
            field=models.FloatField(blank=True, null=True, verbose_name='重量3'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_4',
            field=models.FloatField(blank=True, null=True, verbose_name='重量4'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_5',
            field=models.FloatField(blank=True, null=True, verbose_name='重量5'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_6',
            field=models.FloatField(blank=True, null=True, verbose_name='重量6'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_7',
            field=models.FloatField(blank=True, null=True, verbose_name='重量7'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_8',
            field=models.FloatField(blank=True, null=True, verbose_name='重量8'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='weight_9',
            field=models.FloatField(blank=True, null=True, verbose_name='重量9'),
        ),
    ]
