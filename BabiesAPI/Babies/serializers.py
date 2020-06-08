from rest_framework import serializers
from Babies.models import Baby
from Events.serializers import EventSerializer

class BabySerializer(serializers.ModelSerializer):
	class Meta:
		model = Baby
		fields = '__all__'

class BabyByIdSerializer(serializers.ModelSerializer):
	events= EventSerializer(many=True)
	class Meta:
		model = Baby
		fields = ['id','first_name','last_name','age','gender','alergies','events']