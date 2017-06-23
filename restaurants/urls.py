from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
from django.conf.urls import url,include
from gestionrestaurant import views

urlpatterns = [
   url(r'^gestionrestaurant/', include('gestionrestaurant.urls')),
]
