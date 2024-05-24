from django.db import models

# Create your models here.


class Members(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    passw=models.CharField(max_length=30)

    class Meta:
        app_label = 'First'