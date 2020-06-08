from django.db import models
from Babies.models import Baby

# Create your models here.
class Event(models.Model):
	event_type= models.IntegerField(default=1)
	baby_id= models.ForeignKey(Baby, on_delete=models.PROTECT,related_name="events")
	note= models.CharField(max_length=500)
	timestamp= models.DateTimeField(auto_now_add=True, blank=True)
	class Meta:
		db_table='events'
