from rest_framework import serializers
from .models import *


class MealSerializers(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ('id', 'title', 'desc', 'prix')


class RatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id', 'meal', 'user', 'stars')