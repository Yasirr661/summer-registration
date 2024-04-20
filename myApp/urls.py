
from django.urls import path
from . import views

# Define your URL patterns
urlpatterns = [
    path('courses/', views.offer_courses, name='offer_courses'),
]

