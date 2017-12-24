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
    empty_value_display = '-empty-'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
