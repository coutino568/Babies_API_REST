from rest_framework import serializers
from Babies.models import Baby
from Events.serializers import EventSerializer

class BabiesSerializer(serializers.ModelSerializer):
	events= EventSerializer(many=True)
	class Meta:
		model = Baby
		fields - ['id','first_name','last_name','age','gender','alergies','events']

class BabyByIdSerializer(serializers.ModelSerializer):
	events= EventSerializer(many=True)
	class Meta:
		model = Baby
		fields - ['id','first_name','last_name','age','gender','alergies','events']