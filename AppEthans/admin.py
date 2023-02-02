from django.contrib import admin
from .models import StudentContact
# Register your models here.


class StudentContactConfiuration(admin.ModelAdmin):
    model = StudentContact
    list_display = ['id', 'name', 'email', 'subject']
    search_fields = ['id', 'name']
    list_per_page = 50




admin.site.register(StudentContact,StudentContactConfiuration)


