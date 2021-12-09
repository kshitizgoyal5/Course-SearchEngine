from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import CourseSerializer, CreateCourseSerializer
from .models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name':"Kshitiz"})

class CourseView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GetCourse(APIView):
    serializer_class = CourseSerializer
    lookup_url_kwarg = 'search'
    cacheCourseId = None
    cacheVectors = None
    vectorizer = None
    threshold = 0.2

    def make_cache(self):
        df = pd.DataFrame(list(Course.objects.all().values()))
        self.cacheCourseId = df["course_id"]
        self.vectorizer = TfidfVectorizer()
        self.cacheVectors = self.vectorizer.fit_transform(df["course_title"], df["subject"])

    def get(self, request, search=None, format=None):
        df = pd.DataFrame(list(Course.objects.all().values()))
        if search == None:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
        if self.cacheVectors == None:
            self.make_cache()
        query_vec = self.vectorizer.transform([search])
        results = cosine_similarity(self.cacheVectors, query_vec)
        newResults = [[index, score[0]] for index, score in enumerate(results)]
        newResults = sorted(newResults, key=lambda a_entry: a_entry[1]) 
        courses = []
        for index, score in newResults[-10:]:
            if score > self.threshold:
                cur_course_id = self.cacheCourseId.iloc[index]
                queryset = Course.objects.filter(course_id=cur_course_id)
                if queryset.exists():
                    course = Course.objects.get(course_id=cur_course_id)
                    courses.append(CourseSerializer(course).data)
        courses.reverse()
        return Response(courses, status=status.HTTP_200_OK)



            
            
class CreateCourseView(APIView):
    serializer_class = CreateCourseSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            course_id = serializer.data.get("course_id")
            course_title = serializer.data.get("course_title")
            url = serializer.data.get("url")
            is_paid = serializer.data.get("is_paid")
            price = serializer.data.get("price")
            num_subscribers = serializer.data.get("num_subscribers")
            num_reviews = serializer.data.get("num_reviews")
            num_lectures = serializer.data.get("num_lectures")
            level = serializer.data.get("level")
            content_duration = serializer.data.get("content_duration")
            published_timestamp = serializer.data.get("published_timestamp")
            subject = serializer.data.get("subject")
            queryset = Course.objects.filter(course_id=course_id)
            if not queryset.exists():
                course = Course(course_id=course_id, course_title=course_title, url=url,
                is_paid=is_paid, price=price, num_subscribers=num_subscribers,
                num_reviews=num_reviews, num_lectures=num_lectures, 
                level=level, content_duration=content_duration, published_timestamp=published_timestamp,
                subject=subject)
                course.save()
            return Response(CourseSerializer(course).data, status=status.HTTP_201_CREATED)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

    