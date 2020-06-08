from rest_framework import serializers

from Parents.models import Parent 
from Babies.serializers import BabySerializer

class ParentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parent
		fields = '__all__'


class ParentByIdSerializer(serializers.ModelSerializer):
	children= BabySerializer(many=True)
	class Meta:
		model = Parent
		fields = ['id','first_name','last_name','age','contact_number','children']