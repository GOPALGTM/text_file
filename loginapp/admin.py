from django.contrib import admin
from loginapp.models import user

class useradmin(admin.ModelAdmin):
    list_display= ('username','email','fname','lname','password','cpassword')

admin.site.register(user,useradmin)
# Register your models here.
