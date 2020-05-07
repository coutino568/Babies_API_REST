from django.db import models

# Create your models here.
class Parent(object):
	"""docstring for Parent"""

	name = models.CharField(max_length=200)



	def __str__(self, arg):
		return "PARENT : {}".format(self.name)
		