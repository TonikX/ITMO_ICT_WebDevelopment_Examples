# Generated by Django 3.2.10 on 2022-10-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0006_foodgoods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruit', 'Fruit'), ('Meat', 'Meat')], max_length=30),
        ),
    ]
