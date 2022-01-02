from django.urls import path
from django.urls.resolvers import URLPattern

from shop import admin
from . import views


urlpatterns=[

    path('',views.shop,name='shop'),
    path('search/',views.searching,name='search'),
    path('<slug:c_slug>/',views.shop,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodDetails,name='details'),
  
]