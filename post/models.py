from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='documents/%Y/%m/%d/', null=True, blank=True)
	created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='UserCreated')
	created_on = models.DateTimeField(auto_now_add=True)


    
    

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='PostComment')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='UserComment')

class Rating(models.Model):
	Choices = [
                ('1' , '*'),
                ('2' ,  '**'),
                ('3' ,  '***'),
                ('4' ,  '****'),
                ('5' ,  '*****')  
		      ]
	posts_id = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='PostRating')
	users_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='UserRating')
	rate = models.IntegerField(choices = Choices, default=0)

