from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


from .models import *


from .serializers import *


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


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
