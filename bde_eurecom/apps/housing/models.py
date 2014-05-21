# -*- coding: utf-8 -*
from django.db import models
from django.contrib.auth.models import User


        
class House(models.Model):
    accomodation_name = models.CharField(max_length=30, verbose_name="Accomodation Name", help_text="If you don't know what to put, you can write something including the accomodation type and the name of the landlord, like \"Apartment Smith\"", unique=True, null=True, blank=True)
    
    #principal characteristics
    surface = models.PositiveSmallIntegerField(verbose_name="Surface Area *", help_text="in m2")
    ACCOMODATION_TYPES = ((1,"House"), (2,"Apartment"), (3,"Studio"), (4,"Home stay (vie chez l'habitant)"), (5,"Student residence"), (0,"Other"))
    accomodation_type = models.PositiveSmallIntegerField(verbose_name="Accomodation type *", choices=ACCOMODATION_TYPES)
    accomodation_type_other = models.CharField(max_length=20, verbose_name="Other", help_text="Precise your accomodation type here if you have chosen other", null=True, blank=True)
    number_persons = models.PositiveSmallIntegerField(verbose_name="Number of persons *", help_text="Number of persons the house can accomodate")
     
    
    def __unicode__(self):
        return u"%s"%self.accomodation_name

    def as_table(self):
        output = '<table>'
        for field in self._meta.fields:
            output += '<tr><th>%s</th><td>%s</td></tr>' %(field.name, getattr(self, field.name))
            
        output += '</table>'
        return output


class AdditionalInfo(models.Model):

    house = models.OneToOneField(House)

    #general secondary

    floor = models.PositiveSmallIntegerField(verbose_name="Floor *", help_text="Floor of the entrance door, considering that the street is on floor 0")
    disabled_persons = models.BooleanField(verbose_name="Access for disabled persons")
    need_car = models.BooleanField(verbose_name="Need for at least one car")
    parking = models.BooleanField(verbose_name="Parking")
    HEATING_TYPES = ((1,"electricity"), (2,"gas"), (3,"fuel"), (4,"other"))
    heating_type = models.PositiveSmallIntegerField(verbose_name="Type of heating *", choices=HEATING_TYPES)
    climatisation = models.BooleanField(verbose_name="Climatisation")
    furniture_included = models.BooleanField(verbose_name="Furniture included in the accomodation")
    APPRECIATIONS = ((1,"poor"), (2,"fair"), (3,"good"), (4,"excellent"))
    furniture_appreciation = models.PositiveSmallIntegerField(verbose_name="Furniture appreciation *", choices=APPRECIATIONS)

    #around the accomodation
    noise_comment = models.CharField(max_length=300, verbose_name="Noise comment", help_text="Comment the noise atmosphere arround the accomodation (quiet, unexpected noise...)", null=True, blank=True)
    proximity_shops = models.CharField(max_length=300, verbose_name="Proximity shops", help_text="Comment about the shops arround the (advantages of near shops, or drawbacks)", null=True, blank=True)

    #internet
    internet_connexion = models.BooleanField(verbose_name="Internet connexion provided in the accomodation")
    internet_details = models.CharField(max_length=300, verbose_name="Internet details", help_text="Comment on the internet service provided (box, phone, TV...)", null=True, blank=True)

    #outside equipment
    swimming_pool = models.BooleanField(verbose_name="Swimming pool")
    garden = models.BooleanField(verbose_name="Garden")
    outside_equipment_comment = models.CharField(max_length= 400, verbose_name="Outside equipment", help_text="Precise any other out-door equipment or infrastructure (e.g.: ping-pong, tennis...), or add here your comments on the garden and the swimming pool", null=True, blank=True)


class Price(models.Model):

    house = models.OneToOneField(House)

    #price category
    rent_only = models.PositiveSmallIntegerField(verbose_name="Rent only", null=True, blank=True, help_text="Total rent (not divided by the number of persons), in euros")
    service_charge_only = models.PositiveSmallIntegerField(verbose_name="Service charge only (charges)", null=True, blank=True, help_text="Total, in euros")
    rent_with_service_charge = models.PositiveSmallIntegerField(verbose_name="Rent with service charge *", help_text="In euros. This field is only in case you don't have the detail of the rent and the service charge, leave it empty if you filled \"Rent only\" and \"Service charge only\" fields")
    rent_charge_per_person = models.PositiveSmallIntegerField(verbose_name="Rent with service charge per person", editable=False)
    council_tax = models.PositiveSmallIntegerField(verbose_name="Council tax (taxe d'habitation) *")
    through_agency = models.BooleanField(verbose_name="Rent through an agency")
    agency_fees = models.PositiveSmallIntegerField(verbose_name="Angency fees", default=0)
    apl = models.PositiveSmallIntegerField(verbose_name="APL (Housing Benefits)", null=True, blank=True, help_text="APL in euro, for 1 person (you only)")

    #included in price of rent+service charge
    included_gas = models.BooleanField(verbose_name="Gas")
    included_electricity = models.BooleanField(verbose_name="Electricity")
    included_water = models.BooleanField(verbose_name="Water")
    included_internet = models.BooleanField(verbose_name="Internet")
    included_telephone = models.BooleanField(verbose_name="Telephone")
    included_cleaning = models.BooleanField(verbose_name="Cleaning services")

    other_expenses = models.CharField(max_length=400, verbose_name="Other expenses" , help_text="Precise the price of the service charges that are not included and that you have to pay.", null=True, blank=True)

    def save(self):
        print "custom save method called"
        if self.rent_only!=None and self.service_charge_only!=None:
            print "Autocomputing rent+service charges"
            self.rent_with_service_charge = self.rent_only + self.service_charge_only
        self.rent_charge_per_person = self.rent_with_service_charge / self.house.number_persons
        super(Price, self).save()


class Room(models.Model):
    house = models.ForeignKey(House)

    ROOM_TYPES = ((1,"Bedroom"), (2,"Living room"), (3,"Kitchen"), (4,"Studio all-in-one (main room with kitchen)"), (5,"Bathroom without toilets"), (6,"Bathroom with toilets"), (7,"Toilets alone"), (8,"Garage"), (9,"Storeroom"), (10,"Other"))
    room_type = models.PositiveSmallIntegerField(verbose_name="Room type", choices=ROOM_TYPES)
    other_type =  models.CharField(max_length=20, verbose_name="other", null=True, blank=True, help_text="Precise if you selected \"other\" as room type")
    room_surface = models.PositiveSmallIntegerField(verbose_name="Estimation of surface area (if relevent)", null=True, blank=True)

    class Meta:
        ordering = ['room_type']


class Furniture(models.Model):
    house = models.OneToOneField(House)

    #general
    washing_machine = models.BooleanField(verbose_name="Washing machine", default=False)
    clothes_dryer = models.BooleanField(verbose_name="Clothes dryer", default=False)
    drying_rack = models.BooleanField(verbose_name="Drying rack (etendoir)", default=False)

    #kitchen
    dish_washer = models.BooleanField(verbose_name="Dish washer", default=False)
    fridge = models.BooleanField(verbose_name="Fridge", default=False)
    oven = models.BooleanField(verbose_name="Oven", default=False)
    freezer = models.BooleanField(verbose_name="Freezer", default=False)
    micro_wave = models.BooleanField(verbose_name="Micro-wave", default=False)
    toaster = models.BooleanField(verbose_name="Toaster", default=False)
    dishes = models.BooleanField(verbose_name="Dishes", default=False)
    baking_tray = models.BooleanField(verbose_name="Baking tray (plaque de cuisson)", default=False)
    
    #bedrooms
    desk = models.BooleanField(verbose_name="Desk", default=False)
    desk_chair = models.BooleanField(verbose_name="Desk chair", default=False)

    #Living room
    tv = models.BooleanField(verbose_name="TV", default=False)
    # Don't look relevant enough as it is
    #couches = models.BooleanField(verbose_name="Couches", default=False)
    #seats = models.BooleanField(verbose_name="Seats", default=False)
    

    def __unicode__(self):
        return u"%s"%self.oven



class Location(models.Model):

    house = models.OneToOneField(House)

    #address
    address = models.CharField(max_length=30, verbose_name="Address *")
    city = models.CharField(max_length=30, verbose_name="City *")
    postal_code = models.CharField(max_length=5, verbose_name="Postal code *")
    distance_eurecom = models.FloatField(verbose_name="Distance to travel from the accomodation to Eurecom (in km)", help_text="Auto-generate it by clicking your position on the map", null=True, blank=True)
    #coordinates
    latitude = models.FloatField(verbose_name="latitude", help_text="Auto-generate it by clicking your position on the map")
    longitude = models.FloatField(verbose_name="longitude", help_text="Auto-generate it by clicking your position on the map")


    def __unicode__(self):
        return u"(%s,%s)"%(self.latitude, self.longitude)


class Travel(models.Model):
    
    house = models.OneToOneField(House)

    #time of travels (leave empty if unknown values or impossible)
    time_by_car_max = models.PositiveSmallIntegerField(verbose_name="max time by car", null=True, blank=True) 
    time_by_car_min = models.PositiveSmallIntegerField(verbose_name="min time by car", null=True, blank=True) 
    time_by_bus_max = models.PositiveSmallIntegerField(verbose_name="max time by bus", null=True, blank=True) 
    time_by_bus_min = models.PositiveSmallIntegerField(verbose_name="min time by bus", null=True, blank=True) 
    time_by_bike_max = models.PositiveSmallIntegerField(verbose_name="max time by bike", null=True, blank=True) 
    time_by_bike_min = models.PositiveSmallIntegerField(verbose_name="min time by bike", null=True, blank=True) 
    time_by_foot_max = models.PositiveSmallIntegerField(verbose_name="max time by foot", null=True, blank=True) 
    time_by_foot_min = models.PositiveSmallIntegerField(verbose_name="min time by foot", null=True, blank=True) 

    #bus lines
    bus_line_eurecom = models.CharField(max_length=300, verbose_name="Which bus line to go to Eurecom, and any comment about it. Precise if it's not possible to go by bus", null=True, blank=True)
    bus_line_railroad_station = models.CharField(max_length=300, verbose_name="Which bus line to go to the nearest railroad station, and any comment about it. Precise if it's not possible to go by bus", null=True, blank=True)


class Contact(models.Model):
    
    house = models.OneToOneField(House)    

    #landlord contact
    landlord_first_name = models.CharField(max_length=30, verbose_name="Landlord's first name", null=True, blank=True)
    landlord_last_name = models.CharField(max_length=30, verbose_name="Landlord's last name", null=True, blank=True)
    landlord_email = models.CharField(max_length=40, verbose_name="Landlord's email", null=True, blank=True)
    landlord_phone_number = models.CharField(max_length=25, verbose_name="Landlord's phone number", null=True, blank=True)
    landlord_comment_field = models.CharField(max_length=600, verbose_name="Comment about the landlord", null=True, blank=True)
    
    #agency
    agency_name = models.CharField(max_length=40, verbose_name="Agency name", null=True, blank=True)
    agency_comment_field = models.CharField(max_length=600, verbose_name="Comment about the agency", null=True, blank=True)


class Appreciation(models.Model):
    
    house = models.OneToOneField(House)
    
    #General description fields
    general_description = models.CharField(max_length=1000, verbose_name="Give a general description of the accomodation, anything you want to talk about", null=True, blank=True)
    strong_points = models.CharField(max_length=600, verbose_name="Strong points of the accomodation", null=True, blank=True)
    weak_points = models.CharField(max_length=600, verbose_name="Weak points of the accomodation", null=True, blank=True)


class Photo(models.Model):
    house = models.ForeignKey(House)
    img = models.ImageField(upload_to='housing')
    thumbnail = models.ImageField(upload_to='housing/thumbnails', null=True, blank=True)
    descr = models.CharField(max_length=30, verbose_name="Description", null=True, blank=True)
    pos = models.PositiveSmallIntegerField(verbose_name="Position", null=True, blank=True)
    validated = models.BooleanField(default=False)

    class Meta:
        ordering = ['pos']
    
    def __unicode__(self):
        return u"%s"%self.descr

class Contributor(models.Model):
    user = models.OneToOneField(User)
    houses = models.ManyToManyField(House)
    
    def __unicode__(self):
        return u"%s"%self.user.username
