from django.urls import path
from .views import *

urlpatterns = [
    path('nhacungcap/create/', NhaCungCapCreateView.as_view(), name='nhacungcap-create'),     # Thêm nhà cung cấp
    path('nhacungcap/list/', NhaCungCapListView.as_view(), name='nhacungcap-list'),           # Danh sách nhà cung cấp
    path('nhacungcap/update/<int:pk>/', NhaCungCapUpdateView.as_view(), name='nhacungcap-update'), # Sửa nhà cung cấp
    path('nhacungcap/delete/<int:pk>/', NhaCungCapDeleteView.as_view(), name='nhacungcap-delete'), # Xóa nhà cung cấp
]
