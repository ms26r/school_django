from django.core.exceptions import PermissionDenied
from rest_framework import serializers

from .models import LessonStudents

class LessonStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStudents
        fields = "__all__"
    
class LessonStudentsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStudents
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        lesson = validated_data['lesson']
        if user.id == lesson.teacher_id or lesson.is_public == True :
            LessonStudents.objects.create(**validated_data)
            return validated_data
        raise PermissionDenied("You do not have permission")