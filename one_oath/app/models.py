from django.db import models

# Create your models here.

class Login(models.Model):
    uid = models.CharField(max_length=30, primary_key=True,unique=True)
    password = models.CharField(max_length=255)
    student = models.BooleanField(default=False)
    teacher = models.BooleanField(default=False)
    def __str__(self):
        return self.uid

class Student(models.Model):
    uid = models.CharField(max_length=30,primary_key=True,unique=True)
    email = models.EmailField(max_length=255)
    password=models.CharField(max_length=255,default=f"{uid}")
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    sec = models.CharField(max_length=10)
    mobile_num = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.uid


class Teacher(models.Model):
    uid = models.CharField(max_length=30,primary_key=True,unique=True)
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    password=models.CharField(max_length=255,default=f"{uid}")
    mobile_num = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    des = models.CharField(max_length=100,default="None")
    def __str__(self) -> str:
        return self.uid
    
class Assessment(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)

# class Submission(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
#     marks = models.IntegerField()

#     def __str__(self):
#         return f"Submission by {self.student} for {self.assessment}"
class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        unique_together = ['student', 'assessment']

