from django.forms import ModelForm
from .models import HouseUnits, Topic, Maintenance, HouseRequest


# class Houseunitform(ModelForm):
# 	class meta:
# 		model = HouseUnits
# 		fields = '__all__'

class HouseForm(ModelForm):
	class Meta:
		model = HouseUnits
		fields = '__all__'

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = '__all__'


class MaintenanceForm(ModelForm):
	class Meta:
		model = Maintenance
		fields = '__all__'
			
class HouseRequestForm(ModelForm):
	class Meta:
		model = HouseRequest
		fields = '__all__'
