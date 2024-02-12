from rest_framework import serializers

from .models import CategoryLesson

class CategoryLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLesson
        fields = "__all__"
