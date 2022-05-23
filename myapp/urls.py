from django.urls import path

from .views import *
urlpatterns = [
    path('category', CategoryListAPI.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailAPI.as_view(), name='category_detail'),
    path('city', CityListAPI.as_view(), name='city_list'),
    path('city/<int:pk>', CityDeatilAPI.as_view(), name='city_detail'),
    path('', NewsListAPI.as_view(), name='news_list'),
]
