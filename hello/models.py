from django.db import models

# Create your models here.


class Track(models.Model):
    title = models.CharField(max_length=255, default='Open Source')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    Frst_Name = models.CharField(max_length=100, null=False)
    Last_Name = models.CharField(max_length=100, null=False)
    Age = models.IntegerField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    address = models.TextField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_adult(self):
        if self.Age > 18:
            return True
        else:
            return False
    is_adult.boolean = True
    is_adult.short_description = 'Adult'

    # def __str__(self):
    #     return self.Frst_Name + ' ' + self.Last_Name
