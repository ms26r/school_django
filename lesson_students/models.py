from django.db import models
from lesson.models import Lesson
from person.models import Person

class LessonStudents(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, null=True)
    student = models.OneToOneField(Person, on_delete=models.DO_NOTHING, null=True)