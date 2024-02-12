from django.db import models
from category_lesson_content.models import CategoryLessonContent

from lesson.models import Lesson
from lesson_content.validator_file_extension import validate_file_extension, validate_movie_extension

class LessonContent(models.Model):

    title = models.CharField(max_length=30)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryLessonContent, on_delete=models.DO_NOTHING, null=True)
    video = models.FileField(upload_to="media/videos/", validators=[validate_movie_extension], null=True)
    file = models.FileField(upload_to="media/files/", validators=[validate_file_extension], null=True)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)