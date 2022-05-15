from django.db import models

# Create your models here.

class SurveyResponse(models.Model):
    Name= models.TextField(max_length=200)
    Data= models.JSONField()