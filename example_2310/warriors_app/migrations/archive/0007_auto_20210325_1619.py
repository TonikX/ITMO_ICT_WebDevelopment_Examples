# Generated by Django 3.1.2 on 2021-03-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0006_auto_20201122_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrior',
            name='skill',
            field=models.ManyToManyField(blank=True, null=True, related_name='warrior_skils', through='warriors_app.SkillOfWarrior', to='warriors_app.Skill', verbose_name='Умения'),
        ),
    ]
