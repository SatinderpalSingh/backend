from django.db import models

# Create your models here.
import datetime
# Create your models here.
Deptt=[('computer science','CSE'),
('mechanical engg','ME'),
('civil engg','CE'),
('electrical engg','EE'),
('electronics engg','ECE'),
('production engg','PE'),
]

class patent(models.Model):

    Department  = models.CharField(max_length = 20, choices=Deptt, default = 'computer science')
    Obt_fil = models.CharField('Obtained or filed', choices = [('obtained','Obtained'),('filed','Filed')], max_length = 20)
    Patent_title = models.CharField(max_length = 20)
    Patent_type = models.CharField(max_length = 20)
    Patent_application_no = models.CharField(max_length = 20)
    Patent_grant_year = models.CharField(max_length = 20)
    Commercialized = models.CharField(choices = [('yes','YES'),('no','NO')],max_length = 20, default = 'YES')
    Licence_fee = models.IntegerField(max_length=100000)
    Technology_transferred = models.CharField(max_length = 20)
    Organisation_name = models.CharField(max_length = 20)
    Application_date = models.DateField(default=datetime.date.today)
    Application_no = models.CharField(max_length = 20)
    '''
    def __str__(self):
        return self.Mission
    '''
