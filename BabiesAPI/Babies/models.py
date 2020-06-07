from django.db import models
from Babies.models = Baby
# Create your models here.
class Baby(models.Model):
	firstName= models.CharField(max_lenght=200)
	lastName= models.CharField(max_lenght=200)
	age=models.IntegerField(default=0)
	gender=models.CharField(default="Female")
	alergies=models.BoolField(default=False)
	parent=models.ForeignKey(Parent, on_delete = models.PROTECT, related_name ="children")
	class Meta:
		db_table = 'babies'
