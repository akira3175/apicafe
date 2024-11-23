from rest_framework import viewsets
from .models import NhaCungCap
from .serializers import NhaCungCapSerializer

class NhaCungCapViewSet(viewsets.ModelViewSet):
    queryset = NhaCungCap.objects.all()
    serializer_class = NhaCungCapSerializer
