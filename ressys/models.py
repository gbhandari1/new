from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Applicant(models.Model):
    fname                  = models.CharField(max_length = 256)
    lname                  = models.CharField(max_length = 256)
    email                  = models.EmailField(unique =True)
    phone                  = models.CharField(max_length = 20)
    hired                  = models.BooleanField(default=False)
    goal_oriented          = models.TextField()
    improvement_oriented   = models.TextField()
    success_record         = models.TextField()
    culture_fit            = models.TextField()
    communication          = models.TextField()
    ratings                = models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    create_date            = models.DateTimeField(default = timezone.now)
    hired                  = models.BooleanField(default=False)
    hired_date             = models.DateTimeField(blank=True, null=True)


    def hire (self):
        self.hired = True
        self.hired_date = timezone.now()
        self.save()



    def __str__(self):
        name = self.fname + ' ' + self.lname
        return name
