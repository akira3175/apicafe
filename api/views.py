from rest_framework import generics, status
from rest_framework.response import Response
from .models import NhaCungCap
from .serializers import NhaCungCapSerializer

# View để lấy danh sách và thêm nhà cung cấp
class NhaCungCapCreateView(generics.CreateAPIView):
    queryset = NhaCungCap.objects.all()
    serializer_class = NhaCungCapSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Thêm mới thành công!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View để lấy danh sách tất cả nhà cung cấp
class NhaCungCapListView(generics.ListAPIView):
    queryset = NhaCungCap.objects.all()
    serializer_class = NhaCungCapSerializer

# View để cập nhật nhà cung cấp
class NhaCungCapUpdateView(generics.UpdateAPIView):
    queryset = NhaCungCap.objects.all()
    serializer_class = NhaCungCapSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sửa thành công!", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View để xóa nhà cung cấp
class NhaCungCapDeleteView(generics.DestroyAPIView):
    queryset = NhaCungCap.objects.all()
    serializer_class = NhaCungCapSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Xóa thành công!"}, status=status.HTTP_204_NO_CONTENT)
