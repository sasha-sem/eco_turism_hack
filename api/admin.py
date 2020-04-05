from django.contrib.gis import admin as geoadmin
from django.contrib import admin
from django.contrib.gis.admin.widgets import OpenLayersWidget
from django.contrib.gis.admin import OSMGeoAdmin
from api.models import *    
# Register your models here.


@admin.register(Reserves)
class ReservesAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('id', 'name',)

@admin.register(Routes)
class RoutesAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('id', 'name',)


@admin.register(Sights)
class SightsAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('id', 'name',)

@admin.register(ReserveReview)
class ReserveReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating','reserve',)

@admin.register(RouteReview)
class RouteReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating','route',)
@admin.register(userProfile)
class userProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','is_guide',)
ReviewsPictures 
@admin.register(ReviewsPictures)
class ReviewsPicturesAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    readonly_fields = ["reserve"]