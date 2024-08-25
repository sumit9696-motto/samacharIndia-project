from django.urls import path
from . import views


urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('videos/',views.videos),
    path('viewnews/',views.viewnews),
    path('viewmore/',views.viewmore),
    path('newsv/',views.newsv),

]