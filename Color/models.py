from django.db import models

class Color(models.Model):
	name = models.CharField(max_length=20,primary_key=True)
	code = models.CharField(max_length=7)
	def __str__(self):
		return self.name

class Thing(models.Model):
	name = models.CharField(max_length=20)
	color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True)
def __str__(self):
	return self.name + " " + self.color