# Generated by Django 3.1.2 on 2021-10-08 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warrior',
            name='profession',
        ),
        migrations.AlterField(
            model_name='warrior',
            name='skill',
            field=models.ManyToManyField(blank=True, related_name='warrior_skils', through='warriors_app.SkillOfWarrior', to='warriors_app.Skill', verbose_name='Умения'),
        ),
    ]
