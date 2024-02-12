from django.db import models
from lesson.models import Lesson

class LessonPractice(models.Model):
    title = models.CharField(max_length=30)
    last_send = models.DateTimeField()
    description = models.CharField(max_length=255)
    # lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)