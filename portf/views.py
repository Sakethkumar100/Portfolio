from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    """Main portfolio page view"""
    context = {
        'name': 'Chiguru Saketh Kumar',
        'roles': [
            'Full Stack Developer',
            'Machine Learning Enthusiast', 
            'Problem Solver',
            'Creative Thinker'
        ],
        'stats': {
            'problems_solved': 150,
            'projects_built': 10,
            'internships_completed': 3,
            'client_satisfaction': 95
        }
    }
    return render(request, 'portf/index.html', context)

@csrf_exempt
def contact_form(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process contact form data here
            # For now, just return success
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Failed to send message.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
