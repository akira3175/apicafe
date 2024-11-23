from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NhaCungCapViewSet

router = DefaultRouter()
router.register(r'nhacungcap', NhaCungCapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
