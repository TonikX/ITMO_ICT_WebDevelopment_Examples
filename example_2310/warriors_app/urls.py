from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('api/warriors/', WarriorAPIView.as_view()),
    path('api/warrior/create', WarriorCreateAPIView.as_view()),
    path('api/warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('api/warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('api/warrior/update/<int:pk>', WarriorUpdateView.as_view()),

    path('warrior_templ/<int:id>/', get_warrior_data),
    path('warrior_templ/add/', add_warrior),

    path('warriors/', WarriorAPIView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('warriors/list/related/', WarriorListRelatedAPIView.as_view()),
    path('warriors/list/depth/', WarriorListDepthAPIView.as_view()),
    path('warriors/list/nested/', WarriorListNestedAPIView.as_view()),

    path('profession/create/', ProfessionCreateView.as_view())
    path('warrior/create', WarriorCreateAPIView.as_view()),
    path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),

]