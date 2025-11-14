from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscriber
import json

def home(request):
    """
    Renders the main landing page and handles newsletter signup.
    """
    if request.method == 'POST':
        try:
            # Get the email from the POST request
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({'status': 'error', 'message': 'Email is required.'}, status=400)

            # Check if email already exists
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({'status': 'error', 'message': 'This email is already subscribed.'}, status=400)

            # Create and save the new subscriber
            subscriber = Subscriber(email=email)
            subscriber.save()

            # Send a success response
            return JsonResponse({'status': 'success', 'message': 'Thank you! You are on the list.'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    # This handles the initial GET request (just loading the page)
    # This was the line that had the typo
    return render(request, 'index.html')