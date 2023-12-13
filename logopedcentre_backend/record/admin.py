from django.contrib import admin
from .models import Direction, DirectionPoints, Specialist, UserInformation, UserChildrenInformation, SpecialistSchedule, RecordStatus, Record

admin.site.register(Direction)
admin.site.register(DirectionPoints)
admin.site.register(Specialist)
admin.site.register(UserInformation)
admin.site.register(UserChildrenInformation)
admin.site.register(SpecialistSchedule)
admin.site.register(RecordStatus)
admin.site.register(Record)
