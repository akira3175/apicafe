from rest_framework import serializers
from .models import NhaCungCap

class NhaCungCapSerializer(serializers.ModelSerializer):
    class Meta:
        model = NhaCungCap
        fields = '__all__' 
