from django.db import models

# Create your models here.
class Enter_Url(models.Model):
	Url = models.CharField(max_length = 200)


	def __str__(self):
		return self.Url
		