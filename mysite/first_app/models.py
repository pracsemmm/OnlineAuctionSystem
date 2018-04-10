from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class UserProfileInfo(models.Model):
    #create relationship (dont inherit from User!)
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    user_phone_no=models.CharField(max_length=20,blank=True)
    user_age=models.PositiveIntegerField(blank=True)
    type_of_user=models.CharField(max_length=20,default="seller or customer",blank=True)
    def __str__(self):
        return self.user.username

class Product(models.Model):
    seller_name=models.ForeignKey(User,on_delete=models.PROTECT)
    product_image=models.ImageField(upload_to='product_images',blank=True)
    product_name=models.CharField(max_length=50,blank=True)
    product_category=models.CharField(max_length=50,blank=True)
    product_description=models.CharField(max_length=200,blank=True)
    add_time=models.TimeField(blank=True,default=datetime.now())
    min_bid=models.PositiveIntegerField(blank=True)
    time_limit=models.PositiveIntegerField(blank=True)

class Customer_Bid(models.Model):
    customer = models.ForeignKey(UserProfileInfo,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    bid = models.PositiveIntegerField()
