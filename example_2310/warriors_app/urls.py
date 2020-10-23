from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('warriors/list/related/', WarriorListRelatedAPIView.as_view()),
    path('warriors/list/depth/', WarriorListDepthAPIView.as_view()),
    path('warriors/list/nested/', WarriorListNestedAPIView.as_view()),

    path('profession/create/', ProfessionCreateView.as_view())
]