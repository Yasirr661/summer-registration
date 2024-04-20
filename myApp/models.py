from django.db import models

# Create your models here.

class Course(models.Model):
    department = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    course_title = models.CharField(max_length=255)
    credit_hours = models.IntegerField()
    time_building_room = models.CharField(max_length=255)
    final_exam_datetime = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    remarks = models.CharField(max_length=255)

def __str__(self):
    return f"{self.department} - {self.course_code} - {self.course_title} - {self.credit_hours} - {self.time_building_room} - {self.final_exam_datetime} - {self.instructor} - {self.remarks}"

