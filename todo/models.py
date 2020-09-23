from django.db import models


class Todo(models.Model):
	title = models.CharField(max_length=150, blank=True)
	completed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-created',)
	
