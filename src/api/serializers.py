from rest_framework import serializers
from .models import Enter_Url

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enter_Url
		fields = '__all__'