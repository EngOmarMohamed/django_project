from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Track(models.Model):
	name = models.CharField("Track Name", max_length=50)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Student(models.Model):
	first_name = models.CharField("First Name", max_length=200)
	last_name = models.CharField("Last Name", max_length=200)
	age = models.IntegerField("Age")
	track = models.ForeignKey(Track , on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name