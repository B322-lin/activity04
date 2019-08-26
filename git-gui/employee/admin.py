from django.contrib import admin
from .models import Department, Employee, Club, Status, Income

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Club)
admin.site.register(Status)
admin.site.register(Income)