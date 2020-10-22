from django.urls import path
from .views import WarriorAPIView, WarriorCreateAPIView, WarriorDetailsView, WarriorDestroyView, WarriorUpdateView


app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('warrior/create', WarriorCreateAPIView.as_view()),
    path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),
]