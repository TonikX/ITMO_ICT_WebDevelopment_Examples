# Generated by Django 3.2.10 on 2022-10-02 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0004_goodsimage_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
