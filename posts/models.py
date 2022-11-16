# from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank = False, null = False, max_length =14, db_index = True, default = 'Jacob' 
    )

    body = models.CharField(
        'Body', blank = True, null = False, max_length = 14, db_index = True,
    )
    image = CloudinaryField(
        'image', blank=True,null=True,db_index=True
    )
    likecount = models.IntegerField(
        'Like',default=0,null=True,blank=True
    )

    created_at = models.DateTimeField(
        'created DateTime', blank = True, auto_now_add = True
    )