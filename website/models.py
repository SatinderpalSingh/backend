from django.db import models
import reversion
import datetime

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

class goal(models.Model):
    long_term_goals = models.TextField(max_length = 2000)
    short_term_goals = models.TextField(max_length = 2000)

    def __str__(self):
        return "Goal " + str(datetime.datetime.now())

class adm_FeeStructure(models.Model):
    courses = models.CharField(max_length=50)
    semester = models.PositiveSmallIntegerField()
    day_scholar_fee = models.IntegerField()
    boys_hostel_fee = models.IntegerField()
    girls_hostel_fee = models.IntegerField()
    total_fee_for_hosteller_boys = models.IntegerField()
    total_fee_for_hosteller_girls = models.IntegerField()

