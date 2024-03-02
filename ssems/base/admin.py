from django.contrib import admin
from .models import HouseUnits, Topic, Messages,Reviews, Maintenance, HouseRequest
# Register your models here.

admin.site.register(HouseUnits)
admin.site.register(Topic)
admin.site.register(Messages)
admin.site.register(Reviews)
admin.site.register(Maintenance)
admin.site.register(HouseRequest)