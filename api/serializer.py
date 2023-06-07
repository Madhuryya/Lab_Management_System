from django.db.models import fields
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('Sl_No', 'Description_of_Item', 'Location','added_date')
