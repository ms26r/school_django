from rest_framework import permissions, viewsets

from .models import LessonStudents
from .serializers import LessonStudentsPostSerializer, LessonStudentsSerializer

class LessonStudentsViewSet(viewsets.ModelViewSet):
    queryset = LessonStudents.objects.all()
    # serializer_class = LessonStudentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST" :
            return LessonStudentsPostSerializer
        return LessonStudentsSerializer