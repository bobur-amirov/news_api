from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CategorySerializer, CitySerializer, NewsSerializer
from .models import Category, City, News


class CategoryListAPI(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)


class CityListAPI(APIView):
    def get(self, request):
        city = City.objects.all()
        city_serializers = CitySerializer(city, many=True)
        return Response(city_serializers.data)

    def post(self, request):
        city_serializers = CitySerializer(data=request.data)
        if city_serializers.is_valid():
            city_serializers.save()
            return Response(city_serializers.data, status=status.HTTP_201_CREATED)
        return Response(city_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsListAPI(APIView):
     def get(self, request):
         news = News.objects.all()
         news_serializer = NewsSerializer(news, many=True)
         return Response(news_serializer.data)