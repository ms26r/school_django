from rest_framework import permissions, viewsets

from .models import CategoryLessonContent
from .serializers import CategoryLessonContentSerializer

class CategoryLessonContentViewSet(viewsets.ModelViewSet):
    queryset = CategoryLessonContent.objects.all().order_by('created_at')
    serializer_class = CategoryLessonContentSerializer
    permission_classes = [permissions.IsAuthenticated]
