from rest_framework import permissions, viewsets

from person.permissions import CustomModelPermissions

from .models import Lesson
from .serializers import LessonPostSerializer, LessonSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('created_at')
    # serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermissions]

    def get_serializer_class(self):
        if self.request.method == "POST" :
            return LessonPostSerializer
        return LessonSerializer