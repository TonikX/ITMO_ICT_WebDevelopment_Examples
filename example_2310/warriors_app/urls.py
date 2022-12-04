from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include


app_name = "warriors_app"

router = DefaultRouter()
router.register(r'goods_with_viewset',
                GoodsListViewSetView, basename='good_view_set')

urlpatterns = [

    path('goods_list_with_apiview/', GoodsListViewWithApiView.as_view()),
    path('goods_list_with_generic/', GoodsListGenericView.as_view()),
    path('goods_create_with_generic/', GoodsCreateGenericView.as_view()),
    #path('goods_list_with_viewset/', GoodsListViewSetView.as_view()),
    url(r'^', include(router.urls)),
    path('goods_image_many_create/', GoodsImageCreateGenericView.as_view()),
    path('goods_image_create/', GoodsOneImageCreateGenericView.as_view()),


    path('skills/', SkillAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
    path('warriors/', WarriorAPIView.as_view()),
    path('warrior/create', WarriorCreateAPIView.as_view(), name='warrior_create'),
    path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),

    path('warrior_templ/<int:id>/', get_warrior_data),
    path('warrior_templ/add/', add_warrior),

    path('warriors1/', WarriorAPIView.as_view(), name='warriors'),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('warriors/list/related/', WarriorListRelatedAPIView.as_view()),
    path('warriors/list/depth/', WarriorListDepthAPIView.as_view()),
    path('warriors/list/nested/', WarriorListNestedAPIView.as_view()),

    path('profession/create/', ProfessionCreateView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('warrior/create1', WarriorCreateAPIView.as_view()),
    path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),

    path('profession/create_with_warrior', create_prof_and_connect_to_warrior),

]