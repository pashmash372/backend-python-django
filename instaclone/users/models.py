from django.db import models

# Create your models here.

# CharField - varchar
# TextField - text
# IntegerField - int
# BooleanField - bool
# DateTimeField - datetime
# DateField - date
# TimeField - time
# FloatField - float
# DecimalField - decimal
# EmailField - email
# URLField - url
# FileField - file
# ImageField - image
# ForeignKey - foreign key

# https://docs.djangoproject.com/en/4.2/topics/db/models/

# profile=UserProfile.objects.get(user__email='varun@gmail.com')

# .update() - update
# .delete() - delete
# .get() - get one record
# .save() - save

class User(models.Model):
    name = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255,unique=True,null=False)
    phone_number= models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=255,null=False)
    is_active = models.BooleanField(default=False)

    created_on= models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

class UserProfile(models.Model): # one to one
    DEFAULT_PROFILE_PIC = 'https://mywebsite.com/placeholder.png'
    profile_pic_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC)
    bio=models.CharField(max_length=255,blank=True)
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)