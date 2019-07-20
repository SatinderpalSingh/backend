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


class Balance_Sheet(models.Model):
	Files 	= models.FileField(upload_to = "balance_sheets_files", blank = True, null = True)	

class Finance_Committe(models.Model):
	Name 		= models.CharField(max_length = 20)
	Details 	= models.CharField(max_length = 30)
	Designation	= models.CharField(max_length = 10)

class governence_files(models.Model):
	files 		= models.FileField(upload_to = "governence_files", blank = True, null = True)
	gov_type	= models.IntegerField(max_length = 2)

class gov_type_table(models.Model):
	gov_type	= models.CharField(max_length = 50)
	type_id		= models.IntegerField(max_length = 2)


