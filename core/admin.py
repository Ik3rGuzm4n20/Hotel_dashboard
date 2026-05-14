from django.contrib import admin
from .models import Habitacion, Huesped, Reserva, Housekeeping, Mantenimiento

admin.site.register(Habitacion)
admin.site.register(Huesped)
admin.site.register(Reserva)
admin.site.register(Housekeeping)
admin.site.register(Mantenimiento)