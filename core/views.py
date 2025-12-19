from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Job Tracker Backend is running"})
