from django.contrib import admin
from bde_eurecom.apps.housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor

class HouseAdmin(admin.ModelAdmin):
    list_display = ('accomodation_name','surface',)
    list_filter = ('accomodation_name','surface',)
    ordering = ('accomodation_name',)
    search_fields = ('accomodation_name',)

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('house','oven','fridge',)
    list_filter = ('house','oven','fridge',)
    ordering = ('house',)
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude','longitude',)
    list_filter = ('latitude','longitude',)
    ordering = ('latitude','longitude',)
        
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('img','descr','house','validated',)
    list_filter = ('house',)
    ordering = ('house',)
    search_fields = ('house',)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('user',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('house', 'room_type', 'room_surface',) 
    
admin.site.register(House, HouseAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Contributor, ContributorAdmin)
