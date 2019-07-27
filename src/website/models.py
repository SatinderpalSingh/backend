from django.db import models
import reversion
# Create your models here.

@reversion.register()
class mission(models.Model):
    Mission = models.TextField(max_length = 2000)

class vision(models.Model):
    Vision = models.TextField(max_length = 2000)

class history(models.Model):
    History = models.TextField(max_length = 2000)

class goal(models.Model):
    long_term_goals = models.TextField(max_length = 2000)
    short_term_goals = models.TextField(max_length = 2000)

    def __str__(self):
        return "Goal " + str(datetime.datetime.now())

class campus(models.Model):
	description	= models.TextField(max_length = 2000)	

class adm_FeeStructure(models.Model):
    courses = models.CharField(max_length=50)
    semester = models.PositiveSmallIntegerField()
    day_scholar_fee = models.IntegerField()
    boys_hostel_fee = models.IntegerField()
    girls_hostel_fee = models.IntegerField()
    total_fee_for_hosteller_boys = models.IntegerField()
    total_fee_for_hosteller_girls = models.IntegerField()

class principal_desk(models.Model):
    principal_img     = models.ImageField('Upload Image',upload_to='images/')
    principal_name    = models.CharField(max_length = 25)
    principal_message = models.TextField(max_length = 2000)



class Balance_Sheet(models.Model):
	Name	= models.CharField(max_length = 50)
	Files 	= models.FileField(upload_to = "balance_sheets_files", blank = True, null = True)	

class Finance_Committe(models.Model):
	Name 		= models.CharField(max_length = 50)
	Details 	= models.CharField(max_length = 50)
	Designation	= models.CharField(max_length = 10)

class gov_type_table(models.Model):
	gov_type	= models.CharField(max_length = 50)
	type_id		= models.IntegerField(max_length = 2)


class governence_files(models.Model):
	Name_of_file	= models.CharField(max_length = 25)
	files 		= models.FileField(upload_to = "governence_files", blank = True, null = True)
	type_id		= models.ForeignKey(gov_type_table,on_delete=models.CASCADE)

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

#this class give elements  in academics nav

class Academics(models.Model):
    element_Name	=models.CharField(max_length=50)
    element_id		=models.IntegerField()

#this class give types of file under a elements of Academics

class Academics_elements_FileTypes(models.Model):
    element_id		 =models.ForeignKey(Academics,on_delete=models.CASCADE)
    element_fileTypeName =models.CharField(max_length= 50)
    FileTypeId 		 = models.IntegerField()
"""
 this class give files of elements of Acadmics
 follow work as:
 eg.  to get file from Acadmics->Circular and Notices for P.G. students->Open elective (Notice)
    
  
"""
class Academics_files(models.Model):
    FileName 	= models.CharField(max_length = 50)
    File 	= models.FileField('Upload File',upload_to = '') #path to file folder will be added
    FileTypeid 	= models.ForeignKey(Academics_elements_FileTypes,on_delete=models.CASCADE)



"""
below are classes for Examination nav
"""
"""
this classes give detail of coe office 
"""
class Members_of_Examination_Branch(models.Model):
    Committee_members=models.CharField(max_length = 50)
    designation=models.CharField(max_length = 50)

class Software_Automation_Committee(models.Model):
    Committee_members=models.CharField(max_length = 50)
    designation=models.CharField(max_length = 50)

class Supporting_Staff(models.Model):
    Committee_members=models.CharField(max_length = 50)
    designation=models.CharField(max_length = 50)

"""
this class give files of Roll of honer under EXAMINATION nav
"""
class Roll_of_Honour(models.Model):
    fileName = models.CharField(max_length = 50)
    file_ROH = models.FileField(upload_to = 'Roll_of_hrn_files')

"""
below are classes for faculty nav
"""
"""
this class give description of cultural committee
"""
class Cultural_Committee(models.Model):
    description =models.TextField()
"""
this class give achievements of cultural committee
"""
class Cultural_Committee_Achievements(models.Model):
    achievements = models.CharField(max_length=200)


"""
below are classes for Quality work nav
"""
"""
this class give elements under Quality work
"""
class QualityWork_elements(models.Model):
    element_name  = models.CharField(max_length=100)
    element_id	  =models.IntegerField()

"""
this class give file of elements of quality work
"""
class QW_elements_files(models.Model):
   nameOfFile	 =models.CharField(max_length=200)
   elements_file =models.FileField('Upload File',upload_to = '') #path to file folder will be added
   element_id 	 =models.ForeignKey(QualityWork_elements,on_delete=models.CASCADE)

           
