from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Userus)
class UserAdmin(admin.ModelAdmin):
    #fields = ('first_name', 'last_name')
    list_display = ('username','full_name','age','has_reviews',)
    list_filter = ('age',)
    search_fields = ['last_name', 'first_name']

    def full_name(self, obj):
        return "{} {}".format(obj.last_name, obj.first_name)

    def username(self, obj):
        return "{}".format(obj.user.username)

    def has_reviews(self, obj):
        hs = Review.objects.filter(user=obj)
        return len(hs)>0


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'description', 'img',)
    list_filter = ('name',)
    search_fields = ['name']

    def name(self, obj):
        return "{}".format(obj.name)

    def genre(self, obj):
        return "{}".format(obj.genre)

    def description(self, obj):
        return "{}".format(obj.description)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'rating', 'review_date','review_content')
    list_filter = ('rating',)
    search_fields = ['rating']


    def user(self, obj):
        return "{}".format(obj.user)

    def film(self, obj):
        return "{}".format(obj.film)

    def rating(self, obj):
        return "{}".format(obj.rating)

    def review_date(self, obj):
        return "{}".format(obj.review_date)

    def review_content(self, obj):
        return "{}".format(obj.review_content)
