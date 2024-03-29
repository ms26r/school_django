from rest_framework import serializers

from category_lesson.serializers import CategoryLessonSerializer
from person.serializers import PersonSerializer
from .models import Lesson
from person.models import Person

class LessonSerializer(serializers.ModelSerializer):
    # def get_category(self,obj):
    #     print(obj)
    #     return {
    #         "id": obj.category.id,
    #         "name": obj.category.name,
    #     }
    
    # category = serializers.SerializerMethodField("get_category")
    
    category = CategoryLessonSerializer()
    
    students = PersonSerializer(many=True)
    class Meta:
        model = Lesson
        fields = "__all__"


class LessonPostSerializer(serializers.ModelSerializer):
    teacher = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = "__all__"
        fields = ['name', 'is_public', 'category', 'students', 'teacher']

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     validated_data['teacher'] = user
    #     # Lesson.students.create(**validated_data.students)

    #     lesson = Lesson.objects.create(**validated_data)
        
    #     return validated_data

