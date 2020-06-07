from rest_framework import serializers
from Events.models import Event


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'



class EventByIdSerializer(serializers.ModelSerializer):
	class Meta:
		model=Event
		fields='__all__'