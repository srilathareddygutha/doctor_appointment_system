from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def home(request):

    return render(request,'home.html')


# =====================================================
# USERS
# =====================================================

def users(request):

    data = User.objects.all()

    return render(
        request,
        'users.html',
        {'data':data}
    )


# =====================================================
# DOCTORS
# =====================================================

def doctors(request):

    data = Doctor.objects.all()

    return render(
        request,
        'doctors.html',
        {'data':data}
    )


# =====================================================
# PATIENTS
# =====================================================

def patients(request):

    data = Patient.objects.all()

    return render(
        request,
        'patients.html',
        {'data':data}
    )


# =====================================================
# SCHEDULES
# =====================================================

def schedules(request):

    data = Schedule.objects.all()

    return render(
        request,
        'schedules.html',
        {'data':data}
    )


# =====================================================
# SLOTS
# =====================================================

def slots(request):

    data = Slot.objects.all()

    return render(
        request,
        'slots.html',
        {'data':data}
    )


# =====================================================
# APPOINTMENTS
# =====================================================

def appointments(request):

    data = Appointment.objects.all()

    return render(
        request,
        'appointments.html',
        {'data':data}
    )


# =====================================================
# REVIEWS
# =====================================================

def reviews(request):

    data = Review.objects.all()

    return render(
        request,
        'reviews.html',
        {'data':data}
    )


# =====================================================
# NOTIFICATIONS
# =====================================================

def notifications(request):

    data = Notification.objects.all()

    return render(
        request,
        'notifications.html',
        {'data':data}
    )


# =====================================================
# QUERY 1
# Doctors With Fee Greater Than 500
# =====================================================

def expensive_doctors(request):

    data = Doctor.objects.filter(
        consultation_fee__gt=500
    )

    return render(
        request,
        'expensive_doctors.html',
        {'data':data}
    )


# =====================================================
# QUERY 2
# Completed Appointments
# =====================================================

def completed_appointments(request):

    data = Appointment.objects.filter(
        status='Completed'
    )

    return render(
        request,
        'completed_appointments.html',
        {'data':data}
    )


# =====================================================
# QUERY 3
# Notifications Not Read
# =====================================================

def unread_notifications(request):

    data = Notification.objects.filter(
        is_read=False
    )

    return render(
        request,
        'unread_notifications.html',
        {'data':data}
    )
def update_appointment_status(

    request,

    id,

    status
):

    appointment = Appointment.objects.get(

        appointment_id=id
    )

    appointment.status = status

    appointment.save()

    return HttpResponse(

        "Appointment Status Updated Successfully"
    )
def delete_notification(request,id):

    notification = Notification.objects.get(
        notification_id=id
    )

    notification.delete()

    return HttpResponse(
        "Notification Deleted Successfully"
    )
def add_notification(request):

    if request.method == 'POST':

        Notification.objects.create(

            user_id=request.POST['user_id'],

            title=request.POST['title'],

            message=request.POST['message'],

            notification_type=request.POST['type']
        )

        return HttpResponse(
            "Notification Added"
        )

    return render(
        request,
        'add_notification.html'
    )
def appointment_details(request):

    data = Appointment.objects.select_related(
        'patient',
        'doctor'
    )

    return render(
        request,
        'appointment_details.html',
        {'data':data}
    )
def update_doctor_rating(request,id):

    average = Review.objects.filter(

        doctor_id=id

    ).aggregate(

        Avg('rating')

    )

    avg_rating = average['rating__avg']

    doctor = Doctor.objects.get(

        doctor_id=id
    )

    doctor.avg_rating = avg_rating

    doctor.save()

    return HttpResponse(

        "Doctor Rating Updated Successfully"
    )