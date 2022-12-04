from rest_framework import serializers
from .models import *
from .validators import validate_file_extension


class GoodImagesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с одним файлом (изорбражением)
    """

    class Meta:
        model = GoodsImage  # Указатель на модель
        fields = "__all__"  # Указатель на используемые поля


class GoodImagesManyCreateSerializer(serializers.Serializer):
    """
    Сериализатор для работы с несколькими файлами (изорбражением)
    """
    images = serializers.ListField(  # ListField сериализует список объектов
        child=serializers.FileField(max_length=100000,  # FileField - конкретный файл в списке объектов
                                    allow_empty_file=False,
                                    use_url=True,
                                    validators=[validate_file_extension])
        # validators - указывает на валидатор в который
        # передается файл для валидации
    )
    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects,
                                               many=False)  # Ссылка на товар, для которого загружаем изображения

    def create(self, validated_data):
        """
        Переопредение методя create (создание объектов)
        :param validated_data:
            - goods - товар
            - files - список изображений товара (файлы)
        :return:
            - goods - товар
        """
        goods = validated_data.get('goods')
        files = validated_data.pop('images')
        # validated_data - объект хранящий данные после прохождения сериализация
        for file in files:
            # Для каждого сериализованного файла создается запись в таблице GoodsImage с внешним ключем на goods
            file = GoodsImage.objects.create(file=file, goods=validated_data.get('goods'), image_key='dd')
            file.save()
        return goods  # Юзеру возвращается товар с его файлами


class GoodsSerializer(serializers.ModelSerializer):
    images = GoodImagesSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ['id', 'race', 'name']


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        return Profession(**validated_data)


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class WarriorRelatedSerializer(serializers.ModelSerializer):
    # skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    skill = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"

        # добавляем глубину
        depth = 1


class WarriorNestedSerializer(serializers.ModelSerializer):
    # делаем наследование
    profession = ProfessionSerializer()
    skill = SkillSerializer(many=True)

    # уточняем поле
    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)
