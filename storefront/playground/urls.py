from django.urls import path
from . import views
from .views import CourseView, CreateCourseView, GetCourse

urlpatterns = [
    path('hello/', views.say_hello),
    path('home/', CourseView.as_view()),
    path('create-course/', CreateCourseView.as_view()),
    path('get-courses/<str:search>', GetCourse.as_view()),
]