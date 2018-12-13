from django.db import models

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    activate = models.BooleanField() # account status
    def __str__(self):
        return self.name

class Tweet(models.Model):
    tweet_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    text = models.TextField(max_length=140)
    date = models.DateTimeField(("tweet date: "))
    def __str__(self):
        view_string = self.tweet_user.name + ": " + self.text
        return view_string


