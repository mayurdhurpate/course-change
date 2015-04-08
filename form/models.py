from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    air = models.CharField(max_length=70,null=True,blank=True)
    roll = models.CharField(max_length=70,null=True,blank=True)
    ptype = models.CharField(max_length=70,null=True,blank=True)
    branch = models.CharField(max_length=70,null=True,blank=True)
    choice1 = models.CharField(max_length=70,null=True,blank=True)
    choice2 = models.CharField(max_length=70,null=True,blank=True)
    choice3 = models.CharField(max_length=70,null=True,blank=True)
    choice4 = models.CharField(max_length=70,null=True,blank=True)
    choice5 = models.CharField(max_length=70,null=True,blank=True)
    cpi1 = models.CharField(max_length=70,null=True,blank=True)
    def __str__(self):
        return "%s %s %s" % (self.branch,self.name,self.roll)
    def __unicode__(self):
        return u'%s %s %s' % (self.branch,self.name,self.roll)