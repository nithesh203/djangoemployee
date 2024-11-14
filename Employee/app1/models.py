from django.db import models

# Create your models here.


class Employee(models.Model):
    ename=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    image=models.ImageField(upload_to='image', blank=True, null=True)

    def str(self):
        return self.ename