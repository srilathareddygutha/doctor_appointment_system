from django.contrib import admin

from .models import *


admin.site.register(User)

admin.site.register(Doctor)

admin.site.register(Patient)

admin.site.register(Schedule)

admin.site.register(Slot)

admin.site.register(Appointment)

admin.site.register(Review)

admin.site.register(Notification)


