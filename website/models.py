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
"""
this class provide list of type of course
"""
class course_Type_table(models.Model):
    course_type = models.CharField(max_length= 50)
    course_id = models.IntegerField()

"""
this class provide branchs in each course
"""
class branchInCourse(models.Model):
    branch =models.CharField(max_length = 50)
    intake = models.IntegerField()
    course_id = models.ForeignKey(course_Type_table,on_delete=models.CASCADE)
"""
this class gives name and designation of officer and staff in Academics
"""
class Academics_OfficersAndStaff(models.Model)
    name=models.CharField(max_length = 50)
    degsignation=models.CharField(max_length= 50)

"""
this class give academics regulation files
"""
class Academics_Regulations(models.Model)
    AttachmentName = models.CharField(max_length=50)
    Attachment = models.FileField('Upload File',upload_to = '') #path to file folder will be added
    

#Ph.d student under QIP will be added to other files

#this class give child in academics nav

class Academics(models.Model)
    element_Name=models.CharField(max_length=50)
    element_id=models.IntegerField()

#this class give types of file under a elements of Academics

class Academics_elements_FileTypes(models.Model)
    element_id=models.ForeignKey(Academics,on_delete=models.CASCADE)
    element_fileTypeName=models.CharField(max_length= 50)
    FileTypeId = models.IntegerField()
"""
 this class give files of elements of Acadmics
 follow work as:
 eg.  to get file from Acadmics->Circular and Notices for P.G. students->Open elective (Notice)
    
  
"""
class Academics_files(models.Model)
    FileName =models.CharField(max_length = 50)
    File = models.FileField('Upload File',upload_to = '') #path to file folder will be added
    FileTypeid = models.ForeignKey(Academics_elements_FileTypes,on_delete=models.CASCADE)



"""
below are classes for Examination nav
"""
"""
this classes give detail of coe office 
"""
class Members_of_Examination_Branch(models.Model)
    Committee_members=models.CharField(max_length = 50)
    designation=models.CharField(max_length = 50)

class Software_Automation_Committee(models.Model)
    Committee_members=models.CharField(max_length = 50)
    designation=models.CharField(max_length = 50)
    
class Supporting_Staff(models.Model)
    Committee_members=models.CharField(max_length = 50)
    designation=models.CharField(max_length = 50)
       
"""
this class give files of Roll of honer under EXAMINATION nav
"""
class Roll_of_Honour(models.Model)
    fileName = models.CharField(max_length = 50)
    file_ROH =models.FileField('Upload File',upload_to = '') #path to file folder will be added


