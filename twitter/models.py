from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    userid = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    time = models.DateField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    comments = models.IntegerField()
    tweet_text = models.TextField(max_length=1000)