from django.db import models
# from myusers.models import User
from django.contrib.auth.models import User

# Create your models here.

class HouseUnits(models.Model):
	housetype = models.CharField(max_length = 150, null=True)
	bedrooms = models.CharField(max_length = 10,  null=True, blank=True)
	block = models.CharField(max_length = 50, null=True, blank=True)
	rented = models.BooleanField()
	tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	housenumber = models.IntegerField(null=True, blank=True)
	rent = models.DecimalField(max_digits=100000 , decimal_places=2,)
	rentpaid = models.DecimalField(max_digits=100000, decimal_places=2, blank=True, null=True)	
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']

	def __str__(self):
		return self.housetype 		


class HouseRequest(models.Model):
	house = models.ForeignKey(HouseUnits, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	requested = models.BooleanField(null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)



class Topic(models.Model):
	name = models.CharField(max_length = 200, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']



	def __str__(self):
		return self.name


class Messages(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
	tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	message = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']
			
	def __str__(self):
		return self.message


class Maintenance(models.Model):
	house = models.ForeignKey(HouseUnits, on_delete=models.CASCADE)
	natureofrepair = models.CharField(max_length= 250, null=True)
	repaired = models.BooleanField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)	

	class Meta:
		ordering = ['-updated', '-created']
			
	def __str__(self):
		return self.natureofrepair




class Reviews(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	body = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)	

	class Meta:
		ordering = ['-updated', '-created']
			
	def __str__(self):
		return self.body	