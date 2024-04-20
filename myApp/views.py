from django.shortcuts import render
# views.py

from django.http import JsonResponse
from .models import Course

def offer_courses(request):
    # Retrieve offers courses from the database
    offers_courses = Course.objects.all().values()  # Convert queryset to dictionary

    # Return JSON response containing the offers courses data
    return JsonResponse(list(offers_courses), safe=False)