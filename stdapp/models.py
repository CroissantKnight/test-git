from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    std_number = models.CharField(max_length=9)
    gender = models.CharField(
        max_length=6,
        choices=(('Male', 'Male'), ('Female','Female')),
        default='Male'
    )
    age = models.PositiveIntegerField()
    department = models.CharField(
        max_length=50,
        choices=(('cs', 'cs'), ('it', 'it ')),
        default='cs'
    )
    def  __str__(self):
        return self.fname 
    
class Person(models.Model):
    pname = models.CharField(max_length=100)
    page = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    pdepartment = models.CharField(
        max_length=50,
        choices=(('cs', 'cs'), ('it', 'it ')),
        default='cs'
    )
    def __str__(self):
        return self.pname