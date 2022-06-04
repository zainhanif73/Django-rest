from django.contrib import admin
from .models import Admin, Booking, city, hospital , major , doctor , patient 

# Register your models here.
@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ['id' , 'username', 'password']

@admin.register(city)
class city(admin.ModelAdmin):
    list_display = ['id' , 'name']

@admin.register(hospital)
class hospital(admin.ModelAdmin):
    list_display = ['id' , 'name', 'city_id' , 'location' , 'contact']

@admin.register(major)
class major(admin.ModelAdmin):
    list_display = ['id' , 'name']

@admin.register(doctor)
class doctor(admin.ModelAdmin):
    list_display = ['id', 'h_id', 'username' , 'name' ,'password' , 'major_id' , 'dob' , 'contact', 'cnic' , 'address' , 'education' , 'gender' ,
    'm_status' , 'email', 'language' , 'prof_membership', 'about' , 'm_start' , 'm_end' , 'e_start' , 'e_end' , 'a_start' , 'a_end', 'pfees' , 'cfees' , 
    'block_status' , "account_detail"]

@admin.register(patient)
class patient(admin.ModelAdmin):
    list_display = ['id' , 'username' , 'password' , 'name' , 'dob' , 'contact', 'cnic' , 'address' , 'gender' ,'email', 'block_status']

@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = ['id', 'p_id' , 'd_id' , 'date' , 'type', 'status' , 'time' ]
