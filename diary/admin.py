from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Write)
admin.site.register(Answer)

#admin 의 password는 123