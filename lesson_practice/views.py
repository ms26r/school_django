from rest_framework import permissions, viewsets

from .models import LessonPractice
from .serializers import  LessonPracticeSerializer

class LessonPracticeViewSet(viewsets.ModelViewSet):
    queryset = LessonPractice.objects.all()
    serializer_class = LessonPracticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.request.method == "POST" :
    #         return LessonPracticePostSerializer
    #     return LessonPracticeSerializer