from django.db import models


class mission(models.Model):
    Mission = models.TextField(max_length = 1000)

    def __str__(self):
        return self.Mission




