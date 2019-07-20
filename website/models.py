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
    principal_img = models.ImageField('Upload Image',upload_to='images/')
    principal_message = models.TextField(max_length = 2000)

class adm_files:
    files = models.FileField('Upload File',upload_to = 'admission_files/')
    file_id = models.IntegerField(max_length = 10)

class adm_file_types:
        file_type =  models.CharField('File Type',max_length = 50,choices=[('Admission Policy and Process','Admission Policy and Process'),('Information Brochure','Information Brochure'),('Anti Ragging Squad(Campus)','Anti Ragging Squad(Campus)'),('Anti Ragging Squad(Departmental)','Anti Ragging Squad(Departmental)'),('Anti Ragging Squad(Hostel)',('Anti Ragging Squad(Hostel)'))])
        type_id = models.IntegerField()
