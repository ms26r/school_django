from rest_framework import permissions, viewsets

from .models import LessonContent
from .serializers import LessonContentSerializer

class LessonContentViewSet(viewsets.ModelViewSet):
    queryset = LessonContent.objects.all().order_by('created_at')
    serializer_class = LessonContentSerializer
    permission_classes = [permissions.IsAuthenticated]
