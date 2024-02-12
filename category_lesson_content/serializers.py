from rest_framework import serializers

from .models import CategoryLessonContent

class CategoryLessonContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLessonContent
        fields = "__all__"
