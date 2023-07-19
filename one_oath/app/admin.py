from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register( Submission)