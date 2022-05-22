from django.contrib import admin

from .models import City, Category, News

admin.site.register(City)
admin.site.register(Category)
admin.site.register(News)
