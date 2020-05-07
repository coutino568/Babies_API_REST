from django.db import models

# Create your models here.
class Baby(models.Model):
	firstName= models.CharField(max_lenght=200)
	lastName= models.CharField(max_lenght=200)


	def  __str__(self):
		return 'BABY: {}'.format(self.firstName)