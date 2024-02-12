from django.core.exceptions import PermissionDenied
from rest_framework import serializers

from .models import LessonPractice

class LessonPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPractice
        fields = "__all__"
