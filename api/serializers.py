from rest_framework import serializers, permissions
from .models import Admin, Booked, Booking, city, doctor, hospital, major, patient, getLinks
from django.contrib.auth.hashers import make_password, check_password

class AdminSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Admin
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):    
    class  Meta:
        model = city
        fields = '__all__'


class majorSerializer(serializers.ModelSerializer):
    class  Meta:
        model = major
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    city_id = CitySerializer(many=False , read_only=False)
    class  Meta:
        model = hospital
        fields = '__all__'
        depth = 1
        
    def create(self, validated_data):
        city_id = validated_data.pop('city_id')
        tag_instance = city.objects.get_or_create(name=city_id["name"])
        hospital1 = hospital.objects.create(**validated_data , city_id=tag_instance[0]) 
        return hospital1

    def update(self, instance, validated_data):
        city_id = validated_data.pop('city_id')
        tag_instance = city.objects.get_or_create(name=city_id["name"])
        instance.city_id = tag_instance[0]

        instance.name = validated_data['name']
        instance.location = validated_data['location']
        instance.contact = validated_data['contact']
        instance.block_status = validated_data['block_status']
        instance.save()
        return instance
        

class DoctorSerializer(serializers.ModelSerializer):
    
    city_id = CitySerializer(many=False , read_only=False)
    major_id = majorSerializer(many=False , read_only=False)
    h_id = HospitalSerializer(many=False , read_only=False)

    class Meta:
        model = doctor
        fields = '__all__'
        depth = 2
    
    def create(self, validated_data):
        
        h_id = validated_data.pop('h_id')
        major_id = validated_data.pop('major_id')
        city_id = validated_data.pop('city_id')

        city_instance = city.objects.get_or_create(name=city_id["name"])
        major_instance = major.objects.get_or_create(name=major_id["name"])
        h_instance = hospital.objects.get_or_create(name=h_id["name"])
        
        doctor1 = doctor.objects.create(**validated_data, city_id=city_instance[0], major_id=major_instance[0], h_id=h_instance[0] )
        return doctor1
    
    def update(self, instance, validated_data):
        if "h_id" in validated_data:
            h_id = validated_data.pop('h_id')
            instance.h_id = hospital.objects.get_or_create(name=h_id["name"])[0]
        if "major_id" in validated_data:
            major_id = validated_data.pop('major_id')
            instance.major_id = major.objects.get_or_create(name=major_id["name"])[0]
        if "city_id" in validated_data:
            city_id = validated_data.pop('city_id')
            instance.city_id = city.objects.get_or_create(name=city_id["name"])[0]
        if "name" in validated_data:
            instance.name = validated_data["name"]
        if "username" in validated_data:
            instance.username = validated_data["username"]
        if "email" in validated_data:
            instance.email = validated_data["email"]
        if "password" in validated_data:
            instance.password = validated_data["password"]
        if "dob" in validated_data:
            instance.dob = validated_data["dob"]
        if "contact" in validated_data:
            instance.contact = validated_data["contact"]
        if "cnic" in validated_data:
            instance.cnic = validated_data["cnic"]
        if "address" in validated_data:
            instance.address = validated_data["address"]
        if "education" in validated_data:
            instance.education = validated_data["education"]
        if "gender" in validated_data:
            instance.gender = validated_data["gender"]
        if "m_status" in validated_data:
            instance.m_status = validated_data["m_status"]
        if "language" in validated_data:
            instance.language = validated_data["language"]
        if "prof_membership" in validated_data:
            instance.prof_membership = validated_data["prof_membership"]
        if "about" in validated_data:
            instance.about = validated_data["about"]
        if "m_start" in validated_data:
            instance.m_start = validated_data["m_start"]
        if "m_end" in validated_data:
            instance.m_end = validated_data["m_end"]
        if "e_start" in validated_data:
            instance.e_start = validated_data["e_start"]
        if "a_start" in validated_data:
            instance.a_start = validated_data["a_start"]
        if "e_end" in validated_data:
            instance.e_end = validated_data["e_end"]
        if "a_end" in validated_data:
            instance.a_end = validated_data["a_end"]
        if "cfees" in validated_data:
            instance.cfees = validated_data["cfees"]
        if "pfees" in validated_data:
            instance.pfees = validated_data["pfees"]
        if "experience" in validated_data:
            instance.experience = validated_data["experience"]
        if "status" in validated_data:
            instance.status = validated_data["status"]
        if "block_status" in validated_data:
            instance.block_status = validated_data["block_status"]
        if "account_detail" in validated_data:
            instance.account_detail = validated_data["account_detail"]
        instance.save()
        return instance


class patientSerializer(serializers.ModelSerializer):
     class  Meta:
        model = patient
        fields = '__all__'
        depth = 1

        def update(self, instance, validated_data):
            instance.name = validated_data.CharField(max_length=200)
            instance.username = validated_data.CharField(max_length=200)
            instance.email = validated_data.CharField(max_length=300)
            instance.password = validated_data.CharField(max_length=200)
            instance.contact = validated_data.CharField(max_length=200)
            instance.block_status = validated_data.BooleanField(null=True)
            instance.cnic = validated_data.BigIntegerField()
            instance.address = validated_data.CharField(max_length=300)
            instance.gender = validated_data.CharField(max_length=6)
            instance.dob = validated_data.CharField(max_length=30)
            instance.save()
            return instance


class bookedSerializer(serializers.ModelSerializer):
     class  Meta:
        model = Booked
        fields = '__all__'
        depth = 1

        def update(self, instance, validated_data):
            instance.time_date = validated_data.CharField(max_length=200)
            instance.save()
            return instance


class BookingSerializer(serializers.ModelSerializer):
    
    d_id = DoctorSerializer(many=False , read_only=False)
    p_id = patientSerializer(many=False , read_only=False)

    class  Meta:
        model = Booking
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        tdd_id = validated_data.pop('d_id')
        tdp_id = validated_data.pop('p_id')

        tp_id = patient.objects.get_or_create(name=tdp_id['name'])[0]
        td_id = doctor.objects.get_or_create(name=tdd_id['name'])[0]

        doctor1 = Booking.objects.create(**validated_data, d_id=td_id, p_id=tp_id)
        return doctor1

    def update(self, instance, validated_data):
        print(validated_data)
        if "d_id" in validated_data:
            tdd_id = validated_data.pop('d_id')
            instance.d_id = doctor.objects.get_or_create(name=tdd_id["name"])[0]
        if "p_id" in validated_data:
            tdp_id = validated_data.pop('p_id')
            instance.p_id = patient.objects.get_or_create(name=tdp_id["name"])[0]
        
        if "date" in validated_data:
            instance.date = validated_data["date"]
        if "time" in validated_data:
            instance.time = validated_data["time"]
        if "type" in validated_data:
            instance.type = validated_data["type"]
        if "status" in validated_data:
            instance.status = validated_data["status"]
        if "o_status" in validated_data:
            instance.o_status = validated_data["o_status"]
        if "o_proof" in validated_data:
            instance.o_proof = validated_data["o_proof"]

        instance.save()
        return instance


class getLinksSerializer(serializers.ModelSerializer):
    d_id = DoctorSerializer(many=False , read_only=False)
    p_id = patientSerializer(many=False , read_only=False)

    class  Meta:
        model = getLinks
        fields = '__all__'

    def create(self, validated_data):
        tdd_id = validated_data.pop('d_id')
        tdp_id = validated_data.pop('p_id')
        
        tp_id = patient.objects.get_or_create(name=tdp_id['name'])[0]
        td_id = doctor.objects.get_or_create(name=tdd_id['name'])[0]
        data = getLinks.objects.create(**validated_data, d_id=td_id, p_id=tp_id)
        return data
        