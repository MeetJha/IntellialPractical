from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Customer(models.Model):
	id=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)	
	contact_no=models.IntegerField()
	pincode=models.IntegerField()
	def __str__(self):
		return self.first_name +" "+ self.last_name

class Product(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	unit_price=models.DecimalField(max_digits=6, decimal_places=2)	
	def __str__(self):
		return self.name

class Order(models.Model):
	id=models.AutoField(primary_key=True)
	customer_id=models.ForeignKey(Customer, default='0', on_delete=models.CASCADE)
	product_id=models.ForeignKey(Product, default='0', on_delete=models.CASCADE)	
	unit_price=models.DecimalField(max_digits=6, decimal_places=2)	
	qty=models.IntegerField()	
	total_price=models.DecimalField(max_digits=10, decimal_places=2, default='0')	
	created_date=models.DateTimeField(default=timezone.now)				
	def __str__(self):
		return self.customer_id.first_name + " "+self.customer_id.last_name