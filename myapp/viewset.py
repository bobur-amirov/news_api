from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from myapp.models import Category, City, News
from .serializers import CategorySerializer, CitySerializer, NewsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all()

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        news = self.get_queryset()
        news = news.order_by('-views')[:5]
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)