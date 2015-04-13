from django.db import models
from django.core.validators import validate_email,RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.
def validate_choice(choice):
    if choice == "dummy":
        raise ValidationError("You must fill the First Choice")
alphanum = RegexValidator(r'^[0-9a-z A-Z]*$','Only Alphanumeric values are allowed')
num = RegexValidator(r'^[0-9]*$','Only Integer values are allowed')
class Student(models.Model):
    email = models.CharField(unique=True,max_length=150,validators=[validate_email])
    key = models.CharField(unique=True,max_length=70)

    name = models.CharField(max_length=150,null=True,blank=True,default="",validators=[alphanum])
    air = models.CharField(max_length=70,null=True,blank=True,default="",validators=[num])
    roll = models.CharField(max_length=70,null=True,blank=True,default="",validators=[alphanum])
    ptype = models.CharField(max_length=70,null=True,blank=True,default="year4")
    branch = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    spi1= models.CharField(max_length=4,help_text='Fill you first sem SPI here',null=True,blank=True,default="")
    choice1 = models.CharField(max_length=70,null=True,blank=True,default="dummy",)
    choice2 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice3 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice4 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice5 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    flag = models.IntegerField(default=0)
    def __str__(self):
        return "%s %s" % (self.name,self.roll)
    def __unicode__(self):
        return u'%s %s' % (self.name,self.roll)