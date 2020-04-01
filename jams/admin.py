from django.contrib import admin

# Register your models here.
from .models import Jam, JamRequest, JamRequestApproval

admin.site.register(Jam)
admin.site.register(JamRequest)
admin.site.register(JamRequestApproval)