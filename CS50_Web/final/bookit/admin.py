from django.contrib import admin
from .models import User, Professional_User, Service, Time_Slot, Availability

admin.site.register(User)
admin.site.register(Professional_User)
admin.site.register(Service)
admin.site.register(Time_Slot)
admin.site.register(Availability)