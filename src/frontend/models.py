from django.db import models

# Create your models here.

class Enter_Url(models.Model):
	geeks_field = models.URLField(max_length = 200)