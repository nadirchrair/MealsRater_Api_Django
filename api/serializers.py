from rest_framework import serializers
from .models import *


class MealSerializers(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ('id', 'title', 'desc', 'prix', 'no_of_ratings', 'avg_rating')


class RatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id', 'meal', 'user', 'stars')