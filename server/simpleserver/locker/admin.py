from django.contrib import admin
from locker.models import Lock

# Register your models here.
@admin.register(Lock)
class LockAdmin(admin.ModelAdmin):
    pass