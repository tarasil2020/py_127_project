from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Post(models.Model):
    title = models.CharField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    content = models.TextField()
    number_of_likes = models.IntegerField(default=0)
    author = models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    class Meta:
        pass
    def __str__(self):
        return self.title

class Author(AbstractUser):

    first_name= models.CharField(blank=True)
    last_name = models.CharField(blank=True)
    age = models.IntegerField(blank=True,null=True)
    number_of_posts = models.IntegerField(default=0)
    class Meta:
        pass
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    post = models.ForeignKey('Post',on_delete=models.CASCADE,null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    class Meta:
        pass
    def __str__(self):
        return self.text








