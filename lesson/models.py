from django.db import models
from category_lesson.models import CategoryLesson

from person.models import Person

class Practice(models.Model):
    name = models.CharField(max_length=30)


class Lesson(models.Model):

    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(CategoryLesson, on_delete=models.DO_NOTHING, null=True)
    teacher = models.ForeignKey(Person, on_delete=models.DO_NOTHING, null=False, related_name='teacher')
    assistant = models.ForeignKey(Person, on_delete=models.DO_NOTHING, null=True, related_name='assistant')
    students = models.ManyToManyField(Person,related_name='students') 
    is_public = models.BooleanField(default=True)
    
    