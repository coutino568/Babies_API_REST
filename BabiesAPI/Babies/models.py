from django.db import models
from Parents.models import Parent
# Create your models here.
class Baby(models.Model):
	first_name= models.CharField(max_length=200)
	last_name= models.CharField(max_length=200)
	age=models.IntegerField(default=0)
	gender=models.CharField(default="Female", max_length=10)
	alergies=models.BooleanField(default=False)
	parent=models.ForeignKey(Parent, on_delete = models.PROTECT, related_name ="children")
	class Meta:
		db_table = 'babies'
