from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import bde_eurecom
# from housing.forms import LoginForm
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bde_eurecom.apps.main.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^housing/', include('bde_eurecom.apps.housing.urls')),
    url(r'^login/$', 'bde_eurecom.apps.housing.views.user_login', name='login'),
    url(r'^logout/$', 'bde_eurecom.apps.housing.views.user_logout', name='logout'),
) 

if settings.DEBUG == True:
    #to use media files in developpement
    from django.conf.urls.static import static #to use media and static files during developpement
    urlpatterns += static(bde_eurecom.settings.common.MEDIA_URL, document_root=bde_eurecom.settings.common.MEDIA_ROOT, show_indexes=True) + static(bde_eurecom.settings.common.STATIC_URL, document_root=bde_eurecom.settings.common.STATIC_ROOT, show_indexes=True)

