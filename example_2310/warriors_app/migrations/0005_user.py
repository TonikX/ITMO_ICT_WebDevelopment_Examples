# Generated by Django 3.1.2 on 2020-11-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
            ],
        ),
    ]
