from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Admin, Booking, city, doctor, hospital, major, patient, getLinks
from .serializers import AdminSerializer, BookingSerializer, CitySerializer, DoctorSerializer, HospitalSerializer, getLinksSerializer, majorSerializer, patientSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from time import time
from rest_framework.permissions import BasePermission
import jwt, requests, json
import smtplib

class admin_api(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class city_api(viewsets.ModelViewSet):
    queryset = city.objects.all()
    serializer_class = CitySerializer


class major_api(viewsets.ModelViewSet):
    queryset = major.objects.all()
    serializer_class = majorSerializer


class patient_api(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = patientSerializer


@csrf_exempt
def hospitalApi(request , id=None):
    
    if request.method == "GET":
        stu = hospital.objects.all()
        serializer = HospitalSerializer(stu , many=True)
        return JsonResponse(serializer.data , safe=False)

    elif request.method == 'POST':
        pythondata = JSONParser().parse(request)
        s = HospitalSerializer(data=pythondata , many=False)
        if s.is_valid():
            s.save();
            return JsonResponse(s.data, safe=False)
        else:
            return JsonResponse(s.error_messages, safe=False)    
    
    elif request.method == 'PUT':
        pythondata = JSONParser().parse(request)
        stu = hospital.objects.get(id=id)
        s = HospitalSerializer(stu, data=pythondata , many=False)
        if s.is_valid():
            s.save();
            return JsonResponse(s.data, safe=False)
        else:
            return JsonResponse(s.error_messages, safe=False)    

    elif request.method == 'DELETE':
        stu = hospital.objects.filter(id=id)
        if stu:
            stu.delete()
            res = {'msg' : 'Data Deleted'}
        else:
            res = {'msg' : 'Data Not Found'}
        return JsonResponse(res , safe=False)


@csrf_exempt
def doctor_api(request , id=None):

    if request.method == "GET":
        if id==None:
            stu = doctor.objects.all()
            serializer =  DoctorSerializer(stu , many=True)
        else:
            stu = doctor.objects.get(id=id)
            serializer =  DoctorSerializer(stu , many=False)
        return JsonResponse(serializer.data , safe=False)

    elif request.method == "POST":
        pythondata = JSONParser().parse(request)
        print(pythondata)
        s = DoctorSerializer(data=pythondata , many=False)
        if s.is_valid():
            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.starttls()
            server.login('clinicea88@gmail.com', 'clinicea88@2022')
            msg = 'Subject: {}\n\n{}'.format("Request For Doctor Confirmation" , 
            "Someone Just Signup To Clinicea As A Doctor, Open Your Account And Confirm Whether Is He A Doctor Or Not")
            server.sendmail('clinicea88@gmail.com' , "www.zainhanif73@gmail.com" , msg)
            
            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.starttls()
            server.login('clinicea88@gmail.com', 'clinicea88@2022')
            
            msg = 'Subject: {}\n\n{}'.format("Verification For Clinicea" , 
            "Hello, We Just Receive Your Invitation For Signup As A Doctor In Clinicea. We Have Transferred Your Details To Admin. Please Wait For Some Times")
            server.sendmail('clinicea88@gmail.com' , pythondata['email'] , msg)
            
            s.save()
            return JsonResponse(s.data , safe=False)
        else:
            return JsonResponse(s.error_messages , safe=False)

    elif request.method == "PUT":
        pythondata = JSONParser().parse(request)
        print(pythondata)
        stu = doctor.objects.get(id=id)
        s = DoctorSerializer(stu , data=pythondata , many=False)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data , safe=False)
        else:
            return JsonResponse(s.error_messages , safe=False)

    elif request.method == "PATCH":
        pythondata = JSONParser().parse(request)
        stu = doctor.objects.get(id=id)
        s = DoctorSerializer(stu , data=pythondata , many=False , partial=True)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data , safe=False)
        else:
            return JsonResponse(s.error_messages , safe=False)

    elif request.method == "DELETE":
        stu = doctor.objects.filter(id=id)
        if stu:
            stu.delete()
            res = {'msg' : 'Data Deleted'}
        else:
            res = {'msg' : 'Data Not Found'}
        return JsonResponse(res , safe=False)


def doctor_location_api(request, location, specializaion):

    if request.method=="GET":
        stu = doctor.objects.all()
        serializer =  DoctorSerializer(stu , many=True)
        return JsonResponse(serializer.data , safe=False)


@csrf_exempt
def bookingApi(request , id=None):
    
    if request.method == "GET":
        stu = Booking.objects.all()
        serializer = BookingSerializer(stu , many=True)
        return JsonResponse(serializer.data , safe=False)

    elif request.method == 'POST':
        pythondata = JSONParser().parse(request)
        s = BookingSerializer(data=pythondata , many=False)
        if s.is_valid():
            print(pythondata)
            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.starttls()
            server.login('clinicea88@gmail.com', 'clinicea88@2022')
            msg = 'Subject: {}\n\n{}'.format("Booking Confirmation" , 
            "Congratulations, "+ pythondata['p_id']['name']+" Just Booked An Appointment With You, Open Your Account And Confirm It")
            server.sendmail('clinicea88@gmail.com' , pythondata['d_id']['email'] , msg)
            
            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.starttls()
            server.login('clinicea88@gmail.com', 'clinicea88@2022')

            msg = 'Subject: {}\n\n{}'.format("Booking Confirmation" , 
            "Your Booking With "+pythondata['d_id']['name']+" Has Been Confirmed, Wait For Further Details")
            server.sendmail('clinicea88@gmail.com' , pythondata['p_id']['email'] , msg)
            
            s.save();
            return JsonResponse(s.data, safe=False)
        else:
            return JsonResponse(s.error_messages, safe=False)       
    
    elif request.method == 'PUT':
        pythondata = JSONParser().parse(request)
        stu = Booking.objects.get(id=id)
        s = BookingSerializer(stu, data=pythondata , many=False)
        if s.is_valid():
            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.starttls()
            server.login('clinicea88@gmail.com', 'clinicea88@2022')
            msg = 'Subject: {}\n\n{}'.format("Booking Confirmation" , 
            "Your Booking With "+ pythondata['p_id']['name']+" Has Been Reshedule, Open Your Account And Check It")
            server.sendmail('clinicea88@gmail.com' , pythondata['d_id']['email'] , msg)
            
            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.starttls()
            server.login('clinicea88@gmail.com', 'clinicea88@2022')

            msg = 'Subject: {}\n\n{}'.format("Booking Confirmation" , 
            "Your Booking With Dr "+pythondata['d_id']['name']+" Has Been Reshedule, Wait For Further Details")
            server.sendmail('clinicea88@gmail.com' , pythondata['p_id']['email'] , msg)
            
            s.save();
            return JsonResponse(s.data, safe=False)
        else:
            return JsonResponse(s.error_messages, safe=False)    

    elif request.method == 'DELETE':
        
        stu = Booking.objects.filter(id=id)
        if stu:
            stu.delete()
            
            res = {'msg' : 'Data Deleted'}
        else:
            res = {'msg' : 'Data Not Found'}
        return JsonResponse(res , safe=False)

    elif request.method == 'PATCH':
        pythondata = JSONParser().parse(request)
        stu = Booking.objects.get(id=id)
        s = BookingSerializer(stu, data=pythondata , many=False , partial=True)
        if s.is_valid():
            s.save();
            return JsonResponse(s.data, safe=False)
        else:
            return JsonResponse(s.error_messages, safe=False)

@csrf_exempt
def getLink(request):
    def getDetail():
        API_KEY = '6kmdzKU3RO-t_0J5_UUNyw'
        API_SEC = '51FFWSzJNTbF1PMHlYeLhUN45O9n4MbOfrUE'

        meetingId = 1
        def generateToken():
            token = jwt.encode(
                {'iss': API_KEY, 'exp': time() + 5000},
                API_SEC,
                algorithm='HS256'
            )
            return token
        def getUsers():
            headers = {'authorization': 'Bearer %s' % generateToken(),
                    'content-type': 'application/json'}

            r = requests.get('https://api.zoom.us/v2/users/', headers=headers)
            print("\n fetching zoom meeting info now of the user ... \n")
            print(r.text)

        def getMeetingParticipants():
            headers = {'authorization': 'Bearer %s' % generateToken(),
                    'content-type': 'application/json'}
            r = requests.get(
                f'https://api.zoom.us/v2/metrics/meetings/me/participants', headers=headers)
            print("\n fetching zoom meeting participants of the live meeting ... \n")

            print(r.text)

        meetingdetails = {"topic": "The title of your zoom meeting",
                        "type": 2,
                        "start_time": "2019-06-14T10: 21: 57",
                        "duration": "45",
                        "timezone": "Europe/Madrid",
                        "agenda": "test",

                        "recurrence": {"type": 1,
                                        "repeat_interval": 1
                                        },
                        "settings": {"host_video": "true",
                                    "participant_video": "true",
                                    "join_before_host": "False",
                                    "mute_upon_entry": "False",
                                    "watermark": "true",
                                    "audio": "voip",
                                    "auto_recording": "cloud"
                                    }
                        }

        def createMeeting():
            headers = {'authorization': 'Bearer %s' % generateToken(),
                    'content-type': 'application/json'}
            r = requests.post(
                f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(meetingdetails))

            return r.text
        return createMeeting()

    if request.method=="GET":
        stu = getLinks.objects.all()
        serializer = getLinksSerializer(stu, many=True)
        return JsonResponse(serializer.data , safe=False)

    elif request.method=="POST":
        data = getDetail()

        pythondata = JSONParser().parse(request)

        admin_link=data.replace("start_url\":\"","start_url").split("start_url")[1].split("\",\"join_url\":\"")[0]
        join_link=data.replace("start_url\":\"","start_url").split("start_url")[1].split("\",\"join_url\":\"")[1].split("\",")[0]

        pythondata["join_link"]=join_link
        pythondata["admin_link"]=admin_link 
        
        s = getLinksSerializer(data=pythondata , many=False)
        if s.is_valid():
            s.save();
            return JsonResponse(s.data, safe=False)
        else:
            return JsonResponse(s.error_messages, safe=False)
    
