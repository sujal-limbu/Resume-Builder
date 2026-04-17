from django.db import models

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    linkedin = models.CharField(blank=True,max_length=100)
    objective = models.TextField()
    skills = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    profile = models.URLField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}- Resume'