from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Meal(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    prix = models.IntegerField()

    def no_of_ratings(self):
        rating = Rating.objects.filter(meal=self)
        return len(rating)

    def avg_rating(self):
        sum = 0
        rate = Rating.objects.filter(meal=self)
        for x in rate:
            sum = sum + x.stars
        if len(rate) > 0:
            return sum / len(rate)
        else:
            return 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)])

    #  def __str__(self):
    #     return self.stars

    class Meta:
        unique_together = (('user', 'meal'), )
        index_together = (('user', 'meal'), )
