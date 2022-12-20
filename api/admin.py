from django.contrib import admin
from .models import *
# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'user', 'stars']
    list_filter = ['meal', 'user']


class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'prix']
    search_fields = ['title', 'prix']
    list_filter = ['title', 'prix']


admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
