from django.shortcuts import render
from .serializers import RatingSerializers, MealSerializers
from rest_framework import viewsets
from .models import *
# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
