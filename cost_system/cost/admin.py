from django.contrib import admin
from .models import Order, Requisition, WorkTicket

admin.site.register(Order)
admin.site.register(Requisition)
admin.site.register(WorkTicket)