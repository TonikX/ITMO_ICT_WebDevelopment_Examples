from django.contrib import admin
from .models import Warrior, Profession, Skill, SkillOfWarrior, Goods, GoodsImage, FoodGoods, Log

admin.site.register(Warrior)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)
admin.site.register(Goods)
admin.site.register(GoodsImage)
admin.site.register(FoodGoods)
admin.site.register(Log)