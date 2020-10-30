from django.urls import path
from .views import WarriorAPIView, WarriorCreateAPIView, WarriorDetailsView, \
    WarriorDestroyView, WarriorUpdateView, get_warrior_data, add_warrior


app_name = "warriors_app"


urlpatterns = [
    path('api/warriors/', WarriorAPIView.as_view()),
    path('api/warrior/create', WarriorCreateAPIView.as_view()),
    path('api/warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('api/warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('api/warrior/update/<int:pk>', WarriorUpdateView.as_view()),

    path('warrior_templ/<int:id>/', get_warrior_data),
    path('warrior_templ/add/', add_warrior),
]