from django.db import models
from django.contrib.auth.models import User

# DO NOT MAKE MIGRATIONS HERE!!

# Create your models here.
class Lock(models.Model):
    class Meta:
        db_table = "locks"

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(unique=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    allowed_users = models.ManyToManyField(User, related_name='allowed_users', through='LockPermissions')

class LockPermissions(models.Model):
    class Meta:
        db_table = "lock_permissions"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lock = models.ForeignKey(Lock, on_delete=models.CASCADE)