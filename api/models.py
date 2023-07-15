from django.db import models

# Create your models here.
class Item(models.Model):
	Sl_No = models.CharField(max_length=10)
	Description_of_Item = models.CharField(max_length=100)
	Location = models.CharField(max_length=100)
	added_date=models.DateTimeField(auto_now=True)
	

	def __str__(self) -> str:
		return self.Description_of_Item