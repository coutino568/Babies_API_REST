from django.db import models

# Create your models here.
class Parent(models.Model):
	"""docstring for Parent"""

	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	age=models.IntegerField(default=18)
	contact_number=models.IntegerField(default=1111111111)
	class Meta:
		db_table='parents'
