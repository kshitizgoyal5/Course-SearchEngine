from django.db import models
import datetime

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10, default="", unique=True, null=False, primary_key=True)
    course_title = models.CharField(max_length=100, default="", null=True)
    url = models.URLField(blank=True, null=True, unique=True)
    is_paid = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)
    num_subscribers = models.IntegerField(default=0)
    num_reviews = models.IntegerField(default=0)
    num_lectures = models.IntegerField(default=0)
    level = models.TextField(default="")
    content_duration = models.FloatField(default=0)
    published_timestamp = models.DateTimeField(default=datetime.datetime.now)
    subject = models.TextField(blank=True)
