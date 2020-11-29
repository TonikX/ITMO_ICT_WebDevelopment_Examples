from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.http import Http404
from django.shortcuts import render
from .forms import AddWarrior


from .models import *


from .serializers import *


class SkillAPIView(APIView):

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})



class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created".format(skill_saved.title)})


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})



# в файл serializer.py
# from rest_framework import serializers
# from .models import Warrior
#
#
# class WarriorSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Warrior
#         fields = "__all__"


class ProfessionCreateView(APIView):

    def post(self, request):
        print("REQUEST DATA", request.data)
        profession = request.data.get("profession")
        print("PROF DATA", profession)

        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class WarriorListAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorListRelatedAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorRelatedSerializer


class WarriorListDepthAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorDepthSerializer


class WarriorListNestedAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorNestedSerializer

    def post(self, request):
        serializer = WarriorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        try:
            warrior.delete()
            return Response(status=200)
        except:
            return Response(status=400)


class WarriorCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorDestroyView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorUpdateView(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDetailsView(generics.RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer

# from rest_framework import generics
# Код для юрлов
# path('warrior/create', WarriorCreateAPIView.as_view()),
# path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
# path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
# path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),


def get_warrior_data(request, id):  # отдельная страничка владельца функционально
    try:
        warrior = Warrior.objects.get(id=id)
    except Warrior.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'warrior.html', {'warrior': warrior})


def add_warrior(request):  # ввод владельца функционально
    context = {}

    form = AddWarrior(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'add_warrior.html', context)


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()

