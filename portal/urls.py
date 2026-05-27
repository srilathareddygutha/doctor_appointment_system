from django.urls import path

from . import views


urlpatterns = [

    path('',views.home),

    path('users/',views.users),

    path('doctors/',views.doctors),

    path('patients/',views.patients),

    path('schedules/',views.schedules),

    path('slots/',views.slots),

    path('appointments/',views.appointments),

    path('reviews/',views.reviews),

    path('notifications/',views.notifications),

    path(
        'expensive-doctors/',
        views.expensive_doctors
    ),

    path(
        'completed-appointments/',
        views.completed_appointments
    ),

    path(
        'unread-notifications/',
        views.unread_notifications
    ),
    path(

    'update-appointment/<int:id>/<str:status>/',

    views.update_appointment_status
),
path(
    'delete-notification/<int:id>/',
    views.delete_notification
),
path(
    'add-notification/',
    views.add_notification
),
path(
    'appointment-details/',
    views.appointment_details
),
path(

    'update-rating/<int:id>/',

    views.update_doctor_rating
),
]