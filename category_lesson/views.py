from rest_framework import permissions, viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import CategoryLesson
from .serializers import CategoryLessonSerializer

class CategoryLessonViewSet(viewsets.ModelViewSet):
    queryset = CategoryLesson.objects.all().order_by('created_at')
    serializer_class = CategoryLessonSerializer
    permission_classes = [DjangoModelPermissions]
