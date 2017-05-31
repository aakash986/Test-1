from django.db import models

class query(models.Model):
	question = models.CharField(max_length = 500)
	def __str__(self):
		return self.question

class answer(models.Model):
	reply = models.CharField(max_length = 5)
	def __str__(self):
		return self.reply
