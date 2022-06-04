from pyexpat import model
from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class city(models.Model):
    name = models.CharField(max_length=200)


class major(models.Model):
    name = models.CharField(max_length=300)


class hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    contact = models.CharField(max_length=200)
    city_id = models.ForeignKey(city , on_delete=models.SET_NULL, null=True, related_name='city_id')
    block_status = models.BooleanField(null=True)


class Booked(models.Model):
    time_date = models.CharField(max_length=200)
 

class patient(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    cnic = models.BigIntegerField()
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=6)
    block_status = models.BooleanField(null=True)
    dob = models.CharField(max_length=30)
    

class doctor(models.Model):
    h_id = models.ForeignKey(hospital, on_delete=models.CASCADE, null=True)
    city_id = models.ForeignKey(city, on_delete=models.CASCADE, null=True)
    major_id = models.ForeignKey(major, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    dob = models.CharField(max_length=30)
    contact = models.CharField(max_length=200)
    cnic = models.BigIntegerField()
    address = models.CharField(max_length=300)
    education = models.CharField(max_length=300)
    gender = models.CharField(max_length=6)
    m_status = models.CharField(max_length=7)
    language = models.CharField(max_length=100)
    prof_membership = models.CharField(max_length=100)
    account_detail = models.CharField(max_length=300)
    about = models.CharField(max_length=100)
    m_start = models.FloatField(null=True)
    m_end = models.FloatField(null=True)
    e_start = models.FloatField(null=True)
    e_end = models.FloatField(null=True)
    a_start = models.FloatField(null=True)
    a_end = models.FloatField(null=True)
    cfees = models.IntegerField(null=True)
    pfees = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    block_status = models.BooleanField(null=True)
    status = models.BooleanField(null=True)


class Booking(models.Model):
    p_id   = models.ForeignKey(patient, on_delete=models.CASCADE , null=True) 
    d_id   = models.ForeignKey(doctor , on_delete=models.CASCADE , null=True)
    date   = models.CharField(max_length=200)
    time   = models.FloatField(null=True)
    type   = models.CharField(max_length=200)
    status = models.BooleanField(null=True)
    o_status = models.BooleanField(null=True)
    o_proof = models.CharField(max_length=500, null=True)
    

class getLinks(models.Model):
    p_id   = models.ForeignKey(patient, on_delete=models.CASCADE , null=True) 
    d_id   = models.ForeignKey(doctor , on_delete=models.CASCADE , null=True)
    admin_link   = models.CharField(max_length=1000)
    join_link = models.CharField(max_length=1000)
