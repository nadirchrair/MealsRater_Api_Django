from django.shortcuts import render
from .serializers import RatingSerializers, MealSerializers
from rest_framework import viewsets
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers

    @action(detail=True, methods=['POST'])
    def rate_meal(self, request, pk=None):
        rate = Rating.objects.get(meal_id=pk)
        stars = rate.stars
        if stars:

            meal = Meal.objects.get(id=pk)
            stars = rate.stars
            username = rate.user
            user = User.objects.get(username=username)

            try:
                #update
                rate = Rating.objects.get(user=user.id, meal=meal.id)
                rate.stars = stars
                rate.save()
                serializer = RatingSerializers(rate, many=False)

                json = {
                    'message': 'meal rate updated',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_202_ACCEPTED)

            except:
                #create if the rate not existe
                stars = request.get.data['stars']
                usernam = request.get.data['user']
                usern = User.objects.get(username=usernam)

                rating = Rating.objects.create(meal=meal,
                                               user=usern,
                                               stars=stars)
                serializer = RatingSerializers(rating, many=False)
                json = {
                    'message': 'meal rate create',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)

        else:
            json = {'message': 'there are no stars'}

            return Response(json, status=status.HTTP_204_NO_CONTENT)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
