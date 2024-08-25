from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display =("name","email","mobile","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display =("cname","cpic","cdate")
admin.site.register(category,categoryAdmin)


class desnewsAdmin(admin.ModelAdmin):
    list_display = ("id",'city',"headlines","subject","newsdes","newspic","ndate","ncategory")
admin.site.register(desnews,desnewsAdmin)


class notificationAdmin(admin.ModelAdmin):
    list_display=("id",'ndes',"ndate")
admin.site.register(notification,notificationAdmin)


class videoAdmin(admin.ModelAdmin):
    list_display=('id','vtittle',"vdes","thumb","vlink","vdate")
admin.site.register(video,videoAdmin)


class sliderAdmin(admin.ModelAdmin):
    list_display=("id","stittle",'sdes',"spic","sdate")
admin.site.register(slider,sliderAdmin)


