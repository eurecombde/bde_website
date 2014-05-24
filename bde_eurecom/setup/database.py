from bde_eurecom.apps.housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from random import randint
import random

# ADMIN
u = User(username="WTFO", is_staff=True, is_superuser=True)
u.set_password("company")
u.save()
c = Contributor(user=u)
c.save()


# DATAS
h1 = House(accomodation_name="TCup", surface=95, accomodation_type=2, number_persons=4)
h1.save()

ad1 = AdditionalInfo(house=h1, floor=0, disabled_persons=False, need_car=True, parking=True, heating_type=1, climatisation=False, furniture_included=True, furniture_appreciation=3, noise_comment="The residence is very calm, the house is located far from the street, so almost always quiet.", proximity_shops="There is a grocery at 30m of the residence, useful for buying some bread without without having to take the car.", internet_connexion=True, internet_details="There is a SFR box providing TV and WIFI, phone is included as well. The internet speed is not very high (350kB/s)", swimming_pool= True, garden= True, outside_equipment_comment="We have access to two tennis courts, a ping-pong table in a room, and a petanque strip.")
ad1.save()

p1 = Price(house=h1, rent_only=1995, service_charge_only=0, rent_with_service_charge=1995, council_tax=0, through_agency=False, agency_fees=0, included_gas=False, included_electricity=True, included_water=True, included_internet=True, included_telephone=True, included_cleaning=False, other_expenses="No other expenses or service charge not included", apl=90)
p1.save()

l1 = Location(house=h1, address="760 Chemin de la Tire", city="Mougins", postal_code="06250", distance_eurecom=6.8, latitude=43.608522, longitude=7.012347)
l1.save()

t1 = Travel(house=h1, bus_line_eurecom="It is possible to go to Eurecom by bus with the line 650, but there are very few buses which go to Eurecom", bus_line_railroad_station="Line 630 to go to the railroad station at Cannes", time_by_car_min=15, time_by_car_max=25, time_by_bus_min=20, time_by_bus_max=40, time_by_bike_min=20, time_by_bike_max=30)
t1.save()

ap1 = Appreciation(house=h1, general_description="This apartment is attached to a little building but is more like a house as the door opens directly on the outside, and there is an other opening on a patio and a private garden. The accommodation is within a very nice residence which is well maintained. The apartment is in good condition, well balanced and very convivial for collocation. We found a way to go to the school by bike when the weather is good, there are some bike lanes on the major part of the travel.", strong_points="Proximity to the school.\nVery little traffic jam between it and Eurecom.\nVery good infrastructures, large swimming pool and tennis courts.\nMultiple bathrooms", weak_points="Difficulty to park more than one car.")
ap1.save()

contact1 = Contact(house=h1, landlord_first_name="Roxanna", landlord_last_name="Draycott", landlord_email="draycottr@aol.com", landlord_phone_number="+44 208 954 3818", landlord_comment_field="The landlord lives in London. She is super nice and always disposed to help us with anything we need. It's really a pleasure to have her as landlord.")
contact1.save()


#p11 = Photo(img="housing/TCup-1.jpg", thumbnail="housing/thumbnails/TCup-1.jpg", descr="Living Room", house=h1, pos=2)
#p11.save()
#p12 = Photo(img="housing/TCup-2.jpg", thumbnail="housing/thumbnails/TCup-2.jpg", house=h1, pos=3)
#p12.save()
#p13 = Photo(img="housing/TCup-3.jpg", thumbnail="housing/thumbnails/TCup-3.jpg", house=h1, pos=4)
#p13.save()
#p14 = Photo(img="housing/TCup-4.jpg", thumbnail="housing/thumbnails/TCup-4.jpg", descr="Kitchen", house=h1, pos=5)
#p14.save()
#p15 = Photo(img="housing/TCup-5.jpg", thumbnail="housing/thumbnails/TCup-5.jpg", house=h1, pos=6)
#p15.save()
#p16 = Photo(img="housing/TCup-6.jpg", thumbnail="housing/thumbnails/TCup-6.jpg", descr="Patio", house=h1, pos=1)
#p16.save()


# Adding permission to contributor
content_type = ContentType.objects.get(app_label='housing', model='house')
permission = Permission.objects.create(codename='update_house_{0}'.format(h1.id),
                                       name='Update house "{0}"'.format(h1.accomodation_name),
                                       content_type=content_type)
u1 = User(username="Bastien")
u1.set_password("azerty")
u1.save()
u1.user_permissions.add(permission)
c1 = Contributor(user=u1)
c1.save()
c1.houses.add(h1)

u1_2 = User(username="Geoffrey")
u1_2.set_password("azerty")
u1_2.save()
u1_2.user_permissions.add(permission)
c1_2 = Contributor(user=u1_2)
c1_2.save()
c1_2.houses.add(h1)

f1 = Furniture(house=h1, washing_machine=True, clothes_dryer=False, drying_rack=True, dish_washer=True, fridge=True, oven=True, freezer=True, micro_wave=True, toaster=True, dishes=True, baking_tray=True, desk=True, desk_chair=True, tv=True)
f1.save()

Room(house=h1, room_type=2, room_surface=25).save()
Room(house=h1, room_type=3, room_surface=6).save()
Room(house=h1, room_type=1, room_surface=12).save()
Room(house=h1, room_type=1, room_surface=12).save()
Room(house=h1, room_type=1, room_surface=12).save()
Room(house=h1, room_type=5, room_surface=3).save()
Room(house=h1, room_type=6, room_surface=3).save()
Room(house=h1, room_type=6, room_surface=7).save()
Room(house=h1, room_type=7).save()

# Random houses for search
cities=["Antibes", "Nice", "Cannes", "Valbonne", "Mougins", "Biot", "Roquefort-les-Pins"]

for num in range (10):
    num_persons = randint(1,6)
    surface_per_person = randint(10,30)
    name = "RandHouse"+str(num)
    h_type= randint(1,5)
    h_rand = House(accomodation_name=name, surface=surface_per_person*num_persons, accomodation_type=h_type, number_persons=num_persons)
    h_rand.save()
    
    need_car = random.choice([True, False])
    AdditionalInfo(house=h_rand, floor=0, disabled_persons=False, need_car=need_car, parking=True, heating_type=1, climatisation=False, furniture_included=True, furniture_appreciation=3, internet_connexion=True, swimming_pool= True, garden= True).save()
    
    price_per_person= randint(20,70)*10
    Price(house=h_rand, rent_with_service_charge=price_per_person*num_persons, council_tax=0, through_agency=False, agency_fees=0, included_gas=False, included_electricity=True, included_water=True, included_internet=True, included_telephone=True, included_cleaning=False, apl=90).save()
    
    city=randint(0,6)
    distance= randint(1,30)
    latitude=random.gauss(43.614252, 0.08)
    longitude=random.gauss(7.072984, 0.08)
    Location(house=h_rand, address="Somewhere", city=cities[city], postal_code="00000", distance_eurecom=distance, latitude=latitude, longitude=longitude).save()
