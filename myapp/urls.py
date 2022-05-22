from django.urls import path

from .views import *
urlpatterns = [
    path('category', CategoryListAPI.as_view(), name='category_list'),
    path('city', CityListAPI.as_view(), name='city_list'),
    path('', NewsListAPI.as_view(), name='news_list'),
]
