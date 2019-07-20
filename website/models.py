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

class history(models.Model):
    History = models.TextField(max_length = 2000)

class principal_desk(models.Model):
    principal_img = models.ImageField(upload_to='images/')
    principal_message = models.TextField(max_length = 2000)
