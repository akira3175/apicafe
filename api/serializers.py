from rest_framework import serializers
from .models import NhaCungCap
import re

class NhaCungCapSerializer(serializers.ModelSerializer):
    class Meta:
        model = NhaCungCap
        fields = ['MaNCC', 'TenNCC', 'DiaChi', 'SDT', 'Fax', 'TrangThai']
    
    # Custom validation cho từng field
    def validate_TenNCC(self, value):
        if not value.strip():
            raise serializers.ValidationError("Tên nhà cung cấp không được để trống.")
        return value
    
    def validate_DiaChi(self, value):
        if not value.strip():
            raise serializers.ValidationError("Địa chỉ không được để trống.")
        return value
    
    def validate_SDT(self, value):
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError("Số điện thoại phải là chuỗi 10 chữ số.")
        return value
    
    def validate_Fax(self, value):
        if not value.strip():
            raise serializers.ValidationError("Fax không được để trống.")
        return value