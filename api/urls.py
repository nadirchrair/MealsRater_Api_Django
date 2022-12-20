from django.urls import path, include
from api.views import RatingViewSet, MealViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('meal', MealViewSet, basename='Meal')
router.register('rating', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]
