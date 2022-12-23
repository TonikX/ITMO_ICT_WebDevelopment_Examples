from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from .models import Goods, Log


@receiver(post_save, sender=Goods)
def after_create_good(sender, instance, created, **kwargs):
    """
    Сигнал, вызываемый ПОСЛЕ создания объекта

    :param sender: Объект модели данных, на отслежтивание действий над которым настроен триггер
    :param instance: Экземпляр объекта во время срабатывания триггера
    :param created: Если этот параметр существует, объект создан сейчас
    """
    print('instance', instance)
    print('created', created)
    print('sender', sender)
    if created:
        Log.objects.create(
            message=f"Сигнал, вызываемый после создания товара вызван"
        )


@receiver(pre_save, sender=Goods)
def before_update_good(sender, instance, **kwargs):
    """
    Триггер вызываемый ДО сохранения объекта

    :param sender: Объект модели данных, на отслеживание действий над которым настроен триггер
    :param instance: Экземпляр объекта во время срабатывания триггера
    """
    Log.objects.create(
        message=f"Сигнал, вызываемый до изменения данных о товаре"
    )
    old_instance = Goods.objects.get(id=instance.id)
    print('Old имя товара: ', old_instance.name)
    print('New имя товара: ', instance.name)


@receiver(pre_delete, sender=Goods)
def before_delete_good(sender, instance, **kwargs):
    """
    Триггер вызываемый ДО удаления объекта
    """
    Log.objects.create(
        message=f"Сигнал, вызываемый перед удалением товара"
    )


# @receiver(post_save, sender=Goods)
# def after_create_good(sender, instance, **kwargs):
#     Log.objects.create(
#         message=f"Сигнал, вызываемый после созданием товара вызван"
#     )