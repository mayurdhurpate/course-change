from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.CharField(unique=True,max_length=150)
    key = models.CharField(unique=True,max_length=70)

    name = models.CharField(max_length=150,null=True,blank=True,default="")
    air = models.CharField(max_length=70,null=True,blank=True,default="")
    roll = models.CharField(max_length=70,null=True,blank=True,default="")
    ptype = models.CharField(max_length=70,null=True,blank=True,default="year4")
    branch = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice1 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice2 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice3 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice4 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    choice5 = models.CharField(max_length=70,null=True,blank=True,default="dummy")
    def __str__(self):
        return "%s %s" % (self.name,self.roll)
    def __unicode__(self):
        return u'%s %s' % (self.name,self.roll)