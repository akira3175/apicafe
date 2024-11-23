from django.db import models
from django.contrib.auth.models import AbstractUser

class NhaCungCap(models.Model):
    MaNCC = models.AutoField(primary_key=True)
    TenNCC = models.CharField(max_length=255, null=True, blank=True)
    DiaChi = models.CharField(max_length=255, null=True, blank=True)
    SDT = models.CharField(max_length=20, null=True, blank=True)
    Fax = models.CharField(max_length=20, null=True, blank=True)
    TrangThai = models.IntegerField(default=1)


    class Meta:
        db_table = 'nhacungcap' 

class User(AbstractUser):
    pass