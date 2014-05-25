# -*- coding: utf-8 -*
from django import forms
from bde_eurecom.apps.housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor
from django.contrib.auth.models import User

class HouseForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = House
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(HouseForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            del self.fields['available']

class AdditionalInfoForm(forms.ModelForm):
    required_css_class = 'required'
    
    class Meta:
        model = AdditionalInfo
        exclude = ('house', 'available',)
        widgets = { 
            'noise_comment': forms.Textarea(attrs={'maxlength': model._meta.get_field('noise_comment').max_length}),
            'proximity_shops': forms.Textarea(attrs={'maxlength': model._meta.get_field('proximity_shops').max_length}),
            'internet_details': forms.Textarea(attrs={'maxlength': model._meta.get_field('internet_details').max_length}),
            'outside_equipment_comment': forms.Textarea(attrs={'maxlength': model._meta.get_field('outside_equipment_comment').max_length}),
        }   

class PriceForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Price
        exclude = ('house',)
        widgets = { 
            'other_expenses': forms.Textarea(attrs={'maxlength': model._meta.get_field('other_expenses').max_length}),
        }   


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('house',)


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        exclude = ('house',)


class LocationForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Location
        exclude = ('house', )#'latitude', 'longitude', )
        widgets = { 
            'latitude': forms.TextInput(),
            'longitude': forms.TextInput(),
        }   

class TravelForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Travel
        exclude = ('house',)
        widgets = { 
            'bus_line_eurecom': forms.Textarea(attrs={'maxlength': model._meta.get_field('bus_line_eurecom').max_length}),
            'bus_line_railroad_station': forms.Textarea(attrs={'maxlength': model._meta.get_field('bus_line_railroad_station').max_length}),
        }   


class ContactForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Contact
        exclude = ('house',)
        widgets = { 
            'landlord_comment_field': forms.Textarea(attrs={'maxlength': model._meta.get_field('landlord_comment_field').max_length}),
            'agency_comment_field': forms.Textarea(attrs={'maxlength': model._meta.get_field('agency_comment_field').max_length}),
        }   


class AppreciationForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Appreciation
        exclude = ('house',)
        widgets = { 
            'strong_points': forms.Textarea(attrs={'maxlength': model._meta.get_field('strong_points').max_length}),
            'weak_points': forms.Textarea(attrs={'maxlength': model._meta.get_field('weak_points').max_length}),
            'general_description': forms.Textarea(attrs={'maxlength': model._meta.get_field('general_description').max_length, 'cols':80}),
        }   

        
class ContributorForm(forms.Form):
    contributors = Contributor.objects.all()
    CONTRIBUTORS = [(c.user.id, c.user.username) for c in contributors]
    contributor = forms.ChoiceField(choices=CONTRIBUTORS)


class PhotoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Photo
        exclude = ('house','descr',)
        

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SearchForm(forms.Form):
    # Choices
    ACCOMODATION_TYPES = (('','Accomodation type :'), (1,"House"), (2,"Apartment"), (3,"Studio"), (4,"Home stay (vie chez l'habitant)"), (5,"Student residence"), (0,"Other"))
    NUMBER_PERSONS = (("","Number of persons") ,(1,"1"), (2,"2"), (3,"3"), (4,"4"),(5,"5"),(6,"6"))
    BOOLEAN = (("", ""), (True, "Yes"), (False, "No"))
    PRICE = (("","Price per person"), ("300","<300 €"), ("400","<400 €"), ("500","<500 €"))
    ORDER_BY = (("price__rent_charge_per_person", "Price per person"), ("number_persons", "Number of persons"), ("location__distance_eurecom", "Distance"))
    ORDER = (("", "Increasing"), ("reverse", "Decreasing"))
    # Form
    price__rent_charge_per_person__lte = forms.ChoiceField(label="Price per person (max)", choices=PRICE)
    surface__gte = forms.IntegerField(label="Surface (min)", min_value=0, max_value=9999)
    accomodation_type = forms.ChoiceField(label="Accomodation type", choices=ACCOMODATION_TYPES)
    number_persons = forms.ChoiceField(label="Number of persons", choices=NUMBER_PERSONS)
    additionalinfo__need_car = forms.ChoiceField(label="Need for a car", choices=BOOLEAN)
    order_by = forms.ChoiceField(label="Order by", choices=ORDER_BY)
    order = forms.ChoiceField(choices=ORDER)

class AccountUserForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class AccountContributorForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Contributor
        exclude = ('user','houses')

# class AccountForm(forms.Form):
#     user__first_name = forms.CharField(label="First name", max_length=30)
#     user__last_name = forms.CharField(label="Last name", max_length=30)
#     user__email = forms.CharField(label="E-mail", max_length=100)
#     promo  = forms.IntegerField(label="Promotion", min_value=2013, max_value=2030)
