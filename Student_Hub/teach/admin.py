from django.contrib import admin
from .models import Lesson, Subject
# Register your models here.
admin.site.site_header='STUDENT HUB'
admin.site.site_title = 'STUDENT_HUB'
admin.site.index_title = "Welcome to Student_Hub"


admin.site.register(Subject)
admin.site.register(Lesson)
# admin.site.register(Video)

