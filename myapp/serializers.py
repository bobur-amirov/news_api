from rest_framework import serializers

from .models import Category, City, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'slug']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Siz 3 da belgidan kam belgi kiritdingiz')
        return value

    def validate_slug(self, value):
        if not value.islower():
            raise serializers.ValidationError('slug maydon kichik belgidan iborat emas')
        return value


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'