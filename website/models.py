from django.db import models
import reversion
# Create your models here.
@reversion.register()
class mission(models.Model):
    Mission = models.TextField(max_length = 2000)

    def __str__(self):
        return self.Mission

class vision(models.Model):
    Vision = models.TextField(max_length = 2000)

    def __str__(self):
        return self.Vision

class branchInCourse(models.Model):
    branch =models.CharField(max_length = 50)
    intake = models.IntegerField()
    course_id = models.IntegerField()

class course_Type_table(models.Model):
    course_type = models.CharField(max_length= 50)
    type_id = models.IntegerField()
