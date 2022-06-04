from api import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('cityapi' , views.city_api , basename="city_base")
router.register('adminapi' , views.admin_api , basename="admin_base")
router.register('majorapi' , views.major_api , basename="major_base")
router.register('patientapi' , views.patient_api , basename="patient_base")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('pakistan/doctor/' , views.doctor_api),
    path('pakistan/doctor/<int:id>', views.doctor_api),
    path('pakistan/doctor/update/<int:id>' , views.doctor_api),
    path('pakistan/doctor/<str:location>/<str:specializaion>/' , views.doctor_location_api),
    path('pakistan/doctor/location/specialization/booking/' , views.bookingApi),
    path('booking/' , views.bookingApi),
    path('booking/<int:id>/' , views.bookingApi),
    path('appointments/reschedule/<int:id>/' , views.bookingApi),
    path('pakistan/doctor/location/specialization/booking/<int:id>/' , views.bookingApi),
    path('pakistan/hospital/<int:id>' , views.hospitalApi),
    path('pakistan/hospital/' , views.hospitalApi),
    path("getLink/" , views.getLink)
]
