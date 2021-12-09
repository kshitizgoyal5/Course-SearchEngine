from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("course_id", "course_title", "url", "is_paid",
                "price", "num_subscribers", "num_reviews", "num_lectures",
                "level", "content_duration", "published_timestamp", "subject")

class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("course_id", "course_title", "url", "is_paid",
                "price", "num_subscribers", "num_reviews", "num_lectures",
                "level", "content_duration", "published_timestamp", "subject")
        
        