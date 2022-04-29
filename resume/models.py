from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	phone = models.CharField(max_length=100, null=True)
	text = models.TextField()

	def __str__(self):
		return self.name