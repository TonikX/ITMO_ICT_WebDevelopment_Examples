# Generated by Django 3.2.10 on 2022-11-27 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0010_rename_title_log_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='warriors_app.goods'),
        ),
    ]
