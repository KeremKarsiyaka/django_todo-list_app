from django.db import models


class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)


	def __str__(self):
		if self.completed == True:
			return self.item + ' is completed.'
		else:
			return self.item + ' is waiting to be completed...'