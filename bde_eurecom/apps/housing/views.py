#-*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import CreateView
import json
from bde_eurecom.apps.housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor
from bde_eurecom.apps.housing.forms import HouseForm, AdditionalInfoForm, PriceForm, RoomForm, FurnitureForm, LocationForm, TravelForm, ContactForm, AppreciationForm, PhotoForm, ContributorForm, LoginForm, SearchForm, AccountUserForm, AccountContributorForm
import os
from django.conf import settings
# For thumbnails generation
import rescale
from PIL import Image

import re

# Decorators

def user_permission_house(function):
    """

    """
    def new_function(request, id_house):
        user = request.user
        if user.has_perm('housing.update_house_{0}'.format(id_house)):
            return function(request, id_house)
        else:
            return redirect('/login/?next=%s'%request.path)

    return new_function


@login_required
def home(request):
    """

    """

    # return render(request, 'housing/home.djhtml')
    return redirect('bde_eurecom.apps.housing.views.search_form')

########################################
#                                      #
# SEARCH                               #
#                                      #
########################################

@login_required
def search(request):
    """

    """
    if request.method == 'GET':

        # Dictionary containing the filter
        filter = {'price__isnull':False}
        reverse=False
        order_fields = ["price__rent_charge_per_person"]

        """

        # Code utilisant une syntaxe table__champ__operateur
        # ne semble pas utile
        
        p = re.compile(r'(?P<table>[.a-z]+)__(?P<field>[a-z]+)__(?P<op>[a-z]+)')
        
        for (name,value) in request.GET.iteritems():
            m = p.match(name)
            if m:
                print "%s, %s, %s, %s"%(m.group('table'), m.group('field'), m.group('op'), value)
                filter[m.group('field')+'__'+m.group('op')]=value
        """

        for (name,value) in request.GET.iteritems():
            if name=="order_by":
                order_fields.insert(0,value)

            elif name=="order":
                reverse=True

            else:
                if value=="True":
                    value = True
                elif value=="False":
                    value = False

                filter[name] = value
            

        print "%s"%filter
            
        if reverse:
            order_fields[0] = "-" + order_fields[0]
        
        houses = House.objects.filter(**filter).order_by(*order_fields)

        print "%s"%str(houses)
        
        data = []
        result_rank=1

        for house in houses:
            if house.photo_set.all():  #check if there are photos
                thumbnail_url = house.photo_set.get(pos=1).thumbnail.url
            else:
                thumbnail_url =""
            data.append({
                "id" : house.id,
                "name" : house.accomodation_name,
                "surface" : house.surface,
                "price" : house.price.rent_charge_per_person,
                "thumbnail" : thumbnail_url,
                "number_persons" : house.number_persons,
                "city" : house.location.city,
                "distance" : house.location.distance_eurecom,
                "latitude" : house.location.latitude,
                "longitude" : house.location.longitude,
                "result_rank" : result_rank
            });
            result_rank += 1
            
    return HttpResponse(json.dumps(data), content_type='application/json')

@login_required
def search_form(request):
    """

    """
    if request.method == 'GET':
        search_form = SearchForm()

    return render(request, 'housing/search.djhtml', locals())

@login_required
def quick_search(request):
    """

    """
    if request.method == 'GET':
        term = request.GET['term']
        data = []
        houses = House.objects.filter(accomodation_name__icontains=term)
        for house in houses:
            data.append({
                "value" : house.id,
                "label" : house.accomodation_name,
            });
            
    return HttpResponse(json.dumps(data), content_type='application/json')


########################################
#                                      #
# HOUSE                                #
#                                      #
########################################

@login_required
def house_presentation(request, id_house):
    """

    """
    house = get_object_or_404(House, id=id_house)
    photos = house.photo_set.all()
    rooms = house.room_set.all()
    contributors = house.contributor_set.all()
    
    # relations gathering
    # can implement a function to prevent code reuse
    try:
        additionalinfo = house.additionalinfo
    except ObjectDoesNotExist:
        additionalinfo = AdditionalInfo()
        
    try:
        price = house.price
    except ObjectDoesNotExist:
        price = Price()
        
    try:
        furniture = house.furniture
    except ObjectDoesNotExist:
        furniture = Furniture()
        
    try:
        location = house.location
    except ObjectDoesNotExist:
        location = Location()
        
    try:
        travel = house.travel
    except ObjectDoesNotExist:
        travel = Travel()
        
    try:
        contact = house.contact
    except ObjectDoesNotExist:
        contact = Contact()
    
    try:
        appreciation = house.appreciation
    except ObjectDoesNotExist:
        appreciation = Appreciation()
    
    
    user = request.user
    
    house_form = HouseForm(instance=house, user=user)

    additional_info_form = AdditionalInfoForm(instance=additionalinfo)
    price_form = PriceForm(instance=price)
    furniture_form = FurnitureForm(instance=furniture)
    location_form = LocationForm(instance=location)
    travel_form = TravelForm(instance=travel)
    contact_form = ContactForm(instance=contact)
    appreciation_form = AppreciationForm(instance=appreciation)
    
    if user.has_perm('housing.update_house_{0}'.format(id_house)):
        can_update = True

    return render(request, 'housing/house_presentation.djhtml', locals())


@login_required
def house_create(request):
    """

    """
    if request.method == 'POST': 

        user = request.user
        house_form = HouseForm(request.POST, instance=House(), user=user)
                
        if house_form.is_valid():
            
            house = house_form.save()
            
            if not house.accomodation_name:

                house_name = house.get_accomodation_type_display()
                if not house_name:
                    house_name = house.accomodation_type_other
                
                house.accomodation_name = house_name + "_" + house.landlord_last_name 
            
            house.save()
            
            # Adding permission to contributor
            content_type = ContentType.objects.get(app_label='housing', model='House')
            permission = Permission.objects.create(codename='update_house_{0}'.format(house.id),
                                                   name='Update house "{0}"'.format(house.accomodation_name),
                                                   content_type=content_type)
            user.user_permissions.add(permission)
    
            try:
                contributor = Contributor.objects.get(user=request.user)
                contributor.houses.add(house)
                contributor.save()
            except:
                raise Http404

            return redirect('bde_eurecom.apps.housing.views.house_update', house.id)

    else:
        house_form = HouseForm(user=request.user)

    return render(request, 'housing/house_create.djhtml', locals())

@user_permission_house
def house_update(request, id_house):
    """

    """

    if request.method == 'POST': 
        
        house = get_object_or_404(House, id=id_house)
        
        try:
            additionalinfo = house.additionalinfo
        except ObjectDoesNotExist:
            additionalinfo = AdditionalInfo()
        
        try:
            price = house.price
        except ObjectDoesNotExist:
            price = Price()
        
        try:
            furniture = house.furniture
        except ObjectDoesNotExist:
            furniture = Furniture()
        
        try:
            location = house.location
        except ObjectDoesNotExist:
            location = Location()

        try:
            travel = house.travel
        except ObjectDoesNotExist:
            travel = Travel()
            
        try:
            contact = house.contact
        except ObjectDoesNotExist:
            contact = Contact()

        try:
            appreciation = house.appreciation
        except ObjectDoesNotExist:
            appreciation = Appreciation()
        
        house_form = HouseForm(request.POST, instance=house, user=request.user)
        onetoone_forms = []
        
        onetoone_forms.append(AdditionalInfoForm(request.POST, instance=additionalinfo))
        onetoone_forms.append(PriceForm(request.POST, instance=price))

        onetoone_forms.append(FurnitureForm(request.POST, instance=furniture))
        onetoone_forms.append(LocationForm(request.POST, instance=location))
        onetoone_forms.append(TravelForm(request.POST, instance=travel))
        onetoone_forms.append(ContactForm(request.POST, instance=contact))
        onetoone_forms.append(AppreciationForm(request.POST, instance=appreciation))

        
        print "%s"%str(onetoone_forms)                      
        
        data = "NOT VALID"
    
        if house_form.is_valid() and all(form.is_valid() for form in onetoone_forms):
            data = "VALID"
            house = house_form.save()
            for form in onetoone_forms:
                model = form.save(commit=False)
                model.house = house
                model.save()

        else:
            data = house_form.errors
            for form in onetoone_forms:
                data.update(form.errors)

        return HttpResponse(json.dumps(data), content_type='application/json')
        

    else:
        house = get_object_or_404(House, id=id_house)
        photos = house.photo_set.all()
        rooms = house.room_set.all()
        contributors = house.contributor_set.all()
        
        # relations gathering
        # can implement a function to prevent code reuse
        try:
            additionalinfo = house.additionalinfo
        except ObjectDoesNotExist:
            additionalinfo = AdditionalInfo()
        
        try:
            price = house.price
        except ObjectDoesNotExist:
            price = Price()
        
        try:
            furniture = house.furniture
        except ObjectDoesNotExist:
            furniture = Furniture()
        
        try:
            location = house.location
        except ObjectDoesNotExist:
            location = Location()

        try:
            travel = house.travel
        except ObjectDoesNotExist:
            travel = Travel()
            
        try:
            contact = house.contact
        except ObjectDoesNotExist:
            contact = Contact()

        try:
            appreciation = house.appreciation
        except ObjectDoesNotExist:
            appreciation = Appreciation()

        house_form = HouseForm(instance=house, user=request.user)

        additional_info_form = AdditionalInfoForm(instance=additionalinfo)
        price_form = PriceForm(instance=price)
        room_form = RoomForm()
        furniture_form = FurnitureForm(instance=furniture)
        location_form = LocationForm(instance=location)
        travel_form = TravelForm(instance=travel)
        contact_form = ContactForm(instance=contact)
        appreciation_form = AppreciationForm(instance=appreciation)
        contributor_form = ContributorForm()
                    
    return render(request, 'housing/house_update.djhtml', locals())




########################################
#                                      #
# PHOTOS                               #
#                                      #
########################################

@ensure_csrf_cookie
@user_permission_house  
def add_photo(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        photo_form = PhotoForm(request.POST, request.FILES, instance=Photo())

        if photo_form.is_valid():

            if house.photo_set.all():
                pos = max([photo.pos for photo in house.photo_set.all()])
            else:
                pos = 0
                
            photo = photo_form.save(commit=False)
            photo.house = house
            photo.pos = pos+1
            photo.save()

            # Image resizing
            idir = os.path.join(settings.MEDIA_ROOT, 'housing', 'houses_pictures', str(house.id))
            tdir = os.path.join(idir, 'thumbnails')
            
            if not os.path.exists(idir):
                os.makedirs(idir)
            if not os.path.exists(tdir):
                os.makedirs(tdir)
            
            new_path = os.path.join(idir, '%s-%s.jpg'%(house.accomodation_name, photo.id))
            thumbnail_path = os.path.join(tdir, '%s-%s.jpg'%(house.accomodation_name, photo.id))
            resize_and_thumbnail(photo.img, new_path, thumbnail_path);
            
            os.unlink(os.path.join(settings.MEDIA_ROOT, str(photo.img)))
            
            # Set paths to images
            photo.img = 'housing/houses_pictures/%s/%s-%s.jpg'%(house.id, house.accomodation_name, photo.id)
            photo.thumbnail = 'housing/houses_pictures/%s/thumbnails/%s-%s.jpg'%(house.id, house.accomodation_name, photo.id)
            
            photo.save()
            
            data = {
                "id" : photo.id,
                "img" : photo.img.url,
                "thumbnail" : photo.thumbnail.url,
                "descr" : photo.descr,
                "pos" : photo.pos,
            }
            
        else:
            data = {
                "valid" : False,
            }
    
    return HttpResponse(json.dumps(data), content_type='application/json')
    
@ensure_csrf_cookie
@user_permission_house
def delete_photo(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        photo = get_object_or_404(Photo, id=request.POST['id'])
        if photo.house == house:
            pos = photo.pos
            try:
                os.unlink(os.path.join(settings.MEDIA_ROOT, str(photo.img)))
                os.unlink(os.path.join(settings.MEDIA_ROOT, str(photo.thumbnail)))
            except:
                print "File %s could not be deleted locally"%os.path.join(settings.MEDIA_ROOT, str(photo.img))

            photo.delete()
            for photo in house.photo_set.all():
                if photo.pos > pos:
                    photo.pos = photo.pos-1;
                    photo.save();

            result = {'valid':'true', 'content':'Photo deleted'}
        else:
            result = {'valid':'false', 'content':'House/Photo mismatch'}
    else:
        result = {'valid':'false', 'content':'Not authenticated'}

    return HttpResponse(json.dumps(result), content_type='application/json')

def get_photo(request, id_house):

    if request.method == 'GET':
        house = get_object_or_404(House, id=id_house)
        photos = house.photo_set.all()

    return render(request, 'housing/add_photo.djhtml', locals())

@ensure_csrf_cookie
@user_permission_house
def sort_photo(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        pos = 0
        id = request.POST.get(str(pos), 0)
        while id:
            photo = get_object_or_404(Photo, id=id)
            if photo.house == house:
                photo.pos = pos + 1
                photo.save()
            else:
                print "Photo/House mismatch"
            pos = pos + 1
            id = request.POST.get(str(pos), 0)

    return HttpResponse("")
    

@ensure_csrf_cookie
@user_permission_house
def set_photo_descr(request, id_house):
    """

    """
    if request.method == 'POST':
    
        id = request.POST.get('id', 0)
        descr = request.POST.get('descr', "")
    
        house = get_object_or_404(House, id=id_house)
        photo = get_object_or_404(Photo, id=id)
        
        if photo.house == house:
            photo.descr = descr
            photo.save()
        else:
            print "Photo/House mismatch"
    
    return HttpResponse("")

########################################
#                                      #
# ROOM                                 #
#                                      #
########################################

@ensure_csrf_cookie
@user_permission_house  
def add_room(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        room_form = RoomForm(request.POST, instance=Room())
        
        if room_form.is_valid():
            room = room_form.save(commit=False)
            room.house = house
            room.save()
            
            result = {
                "valid":True,
                "content":'The room has just been added!',
                "id" : room.id,
                "name" : room.get_room_type_display(),
                "other" : room.other_type,
                "surface" : room.room_surface,
            }
            
        else:
            result = {'valid':False, 'content':'The room form is not valid!'}
            
    return HttpResponse(json.dumps(result), content_type='application/json')

@ensure_csrf_cookie
@user_permission_house  
def delete_room(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        id_room = request.POST.get('room', 0)
        
        if id_room:
            room = get_object_or_404(Room, id=id_room)
            room.delete()
            result = {'valid':True, 'content':'The room has been deleted!'}
        else:
            result = {'valid':False, 'content':'The room you try to remove does not exists!'}
    
    return HttpResponse(json.dumps(result), content_type='application/json')


########################################
#                                      #
# CONTRIBUTOR                          #
#                                      #
########################################

@ensure_csrf_cookie
@user_permission_house  
def add_contributor(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        id_user = request.POST.get('user', 0)
        
        if id_user:
            user = get_object_or_404(User, id=id_user)
            # Adding permission to contributor
            permission = Permission.objects.get(codename='update_house_{0}'.format(house.id))
            user.user_permissions.add(permission)
    
            try:
                contributor = get_object_or_404(Contributor, user=user)
                contributor.houses.add(house)
                contributor.save()
                result = {'valid':True, 'content':'%s was added to the contributors'%user.username, 'user':user.username, 'id_user':user.id}
                
            except:
                raise Http404

        else:
            result = {'valid':False, 'content':'The Contributor is not valid'}
                
    return HttpResponse(json.dumps(result), content_type='application/json')

@ensure_csrf_cookie
@user_permission_house  
def delete_contributor(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        id_user = request.POST.get('user', 0)
        
        if id_user:
            user = get_object_or_404(User, id=id_user)
            print "user: %s; del: %s"%(request.user, user)
            
            if user != request.user:
                
                permission = Permission.objects.get(codename='update_house_{0}'.format(house.id))
                user.user_permissions.remove(permission)
                contributor = get_object_or_404(Contributor, user=user)
                contributor.houses.remove(house)
                contributor.save()
                
                result = {'valid':True, 'content':'%s was deleted from the contributors'%user.username}
            
            else:
                result = {'valid':False, 'content':'You cannot remove yourself from the contributors!'}
        else:
            result = {'valid':False, 'content':'No contributor was specified for deletion'}

            

    return HttpResponse(json.dumps(result), content_type='application/json')
    # return render(request, 'housing/add_contributor.djhtml', locals())
    # For the template
    # contributor_form = ContributorForm()
    # contributors = house.contributor_set.all()
    

########################################
#                                      #
# MAP                                  #
#                                      #
########################################

@login_required
def map(request):
    """
    
    """
    return render(request, 'housing/map.djhtml')

@login_required
def precise_position(request):
    """
    
    """
    return render(request, 'housing/precisePosition.djhtml')

@login_required
def mapMarkersAll(request):
    """

    """
    #house = get_object_or_404(House, id=id_house)
    houses = House.objects.all()
    markers = []
    rank=1
    for house in houses:
        location=house.gpscoordinate
        markers.append({"latitude":location.latitude, "longitude":location.longitude, "content":house.accomodation_name, "rank":rank})
        rank+=1

    result = {"markers": markers}
    return HttpResponse(json.dumps(result), content_type='application/json')

@login_required
def mapMarkers(request, id_house):
    """

    """
    house = get_object_or_404(House, id=id_house)
    location=house.gpscoordinate
    markers = []
    markers.append({"latitude":location.latitude, "longitude":location.longitude, "content":house.accomodation_name})
    result = {"markers": markers}
    
    return HttpResponse(json.dumps(result), content_type='application/json')


########################################
#                                      #
# GALLERY                              #
#                                      #
########################################

@login_required
def gallery(request, id_house):
    """

    """
    house = get_object_or_404(House, id=id_house)
    photos = house.photo_set.all()        

    return render(request, 'housing/gallery.djhtml', locals())

########################################
#                                      #
# ACCOUNT                              #
#                                      #
########################################

@login_required
def account(request):
    user = request.user
    try:
        contributor = user.contributor
        houses = contributor.houses.all()
        for house in houses:
            if house.photo_set.all():  #check if there are photos
                house.thumbnail_url = house.photo_set.get(pos=1).thumbnail.url
        account_user_form = AccountUserForm(instance=user)
        account_contributor_form = AccountContributorForm(instance=contributor)

    except:
        contributor = None

    return render(request, 'housing/account.djhtml', locals())

@ensure_csrf_cookie
@login_required
def account_update(request):
    """

    """
    if request.method == 'POST':
        user = request.user
        contributor = get_object_or_404(Contributor, user=user)
        account_user_form = AccountUserForm(request.POST, instance=user)
        account_contributor_form = AccountContributorForm(request.POST, instance=contributor)
        if account_user_form.is_valid() and account_contributor_form.is_valid():
            user = account_user_form.save()
            contributor = account_contributor_form.save()
            result = {'valid':'true', 'content':'Your profile has been updated!'}
        else:
            result = {'valid':'false', 'content':'The form is not valid!'}
    else:
        result = {'valid':'false', 'content':'Not authenticated'}

    return HttpResponse(json.dumps(result), content_type='application/json')

########################################
#                                      #
# USER                                 #
#                                      #
########################################

def user_login(request):
    """

    """
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        next = request.POST['next']
        
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect(next)
            else:
                error = True
                
    else:
        form = LoginForm()
        if 'next' in request.GET:
            next = request.GET['next']
        else:
            next = "/housing"

    return render(request, 'housing/user_login.djhtml', locals())

def user_logout(request):
    """

    """
    logout(request)
    return redirect(reverse(user_login))



def resize_and_thumbnail(img_path, new_path, thumbnail_path):
    """
    Resize and crop an image to fit the specified size.

    """

    wanted_size = (settings.IMG_WIDTH, settings.IMG_HEIGHT)
    thumb_size = (settings.THUMBNAIL_WIDTH, settings.THUMBNAIL_HEIGHT)
    img = Image.open(img_path)

    img_width = img.size[0]
    img_height = img.size[1]
    img_ratio = img_width/float(img_height) 
    wanted_ratio = wanted_size[0]/float(wanted_size[1])   # width/height

    if img_ratio < 1 :  #portrait image
        portrait_size=(int(img_ratio*wanted_size[1]), wanted_size[1])
        img = rescale.rescale(img, portrait_size)

    else:   #landscape image
        if img_ratio < wanted_ratio:    #image too high
            to_cut = int((img_height-img_width/wanted_ratio)/2)
            box = (0, to_cut, img_width, img_height - to_cut)     #(left, top, right, bottom)
            img = img.crop(box)


        elif img_ratio > wanted_ratio:   #image too large
            to_cut = int((img_width-wanted_ratio*img_height)/2)
            box = (to_cut, 0, img_width - to_cut, img_height)    #(left, top, right, bottom)
            img = img.crop(box)

        img = rescale.rescale(img, wanted_size)

    img.save(new_path)
    img = rescale.rescale(img, thumb_size)
    img.save(thumbnail_path)

