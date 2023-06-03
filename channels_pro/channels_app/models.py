from django.db import models

# Create your models here.

class Test(models.Model):
    field_image=models.ImageField(upload_to='images',blank=True)
    field_json=models.JSONField()
    field_file=models.FileField(upload_to='files',blank=True)


