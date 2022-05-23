from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CategorySerializer, CitySerializer, NewsSerializer
from .models import Category, City, News


class CategoryListAPI(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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


class CityDeatilAPI(APIView):

    def city_detail(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        city = self.city_detail(pk)
        city_serializer = CitySerializer(city)
        return Response(city_serializer.data)

    def put(self, request, pk):
        city = self.city_detail(pk)
        city_serializer = CitySerializer(city, data=request.data)
        if city_serializer.is_valid():
            city_serializer.save()
            return Response(city_serializer.data)
        return Response(city_serializer.errors)

    def delete(self, request, pk):
        city = self.city_detail(pk)
        city.delete()
        return Response({'mess': 'delete'})


class NewsListAPI(APIView):
    def get(self, request):
        news = News.objects.all()
        news_serializer = NewsSerializer(news, many=True)
        return Response(news_serializer.data)

    def post(self, request):
        news_serializer = NewsSerializer(data=request.data)
        print(request.data['tags'])
        if news_serializer.is_valid():
            news_serializer.save()
            return Response(news_serializer.data)
        return Response(news_serializer.errors)
