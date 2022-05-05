from django.contrib import admin
from api.models import Student

# Register your models here.
#(step-3)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

