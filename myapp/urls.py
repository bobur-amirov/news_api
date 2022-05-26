from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewset import CategoryViewSet, CityViewSet, NewsViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('city', CityViewSet)
router.register('news', NewsViewSet, basename='news')

from .views import *

urlpatterns = [
    path('', include(router.urls)),
    # path('category', CategoryListAPI.as_view(), name='category_list'),
    # path('category/<int:pk>', CategoryDetailAPI.as_view(), name='category_detail'),
    # path('city', CityListAPI.as_view(), name='city_list'),
    # path('city/<int:pk>', CityDeatilAPI.as_view(), name='city_detail'),
    # path('', NewsListAPI.as_view(), name='news_list'),
    # path('new/<int:pk>', NewsCategoryFilterAPI.as_view(), name='news_category'),
]
