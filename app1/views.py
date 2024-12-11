
def home(request):
    return render(request, "index.html")


import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse

def google_form_view(request):
    return render(request, 'google_form.html')

def handle_response(request):
    if request.method == 'POST':
        user_response = request.POST.get('response')  # Accept or Decline
        name = request.POST.get('name')
        email = request.POST.get('email')
        telegram = request.POST.get('telegram')

        # Google Form Endpoint and Field Mapping
        GOOGLE_FORM_URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSd3jXrd7rw4bnMCu0TpdR8vEQUTwlRcKFj5lLbwTsmT-Vh47Q/formResponse'
        form_data = {
            'entry.132228308': name,  # Replace with the field name for "name"
            'entry.1661919080': email,  # Replace with the field name for "email"
            'entry.1894471568': telegram,
            'entry.847900189': user_response,  # Replace with the field name for "response"
        }

        # Submit data to Google Form
        response = requests.post(GOOGLE_FORM_URL, data=form_data)

        # Redirect based on user's response
        if user_response == 'accept':
            return redirect('next_page')
        elif user_response == 'decline':
            return redirect('error_page')
    return redirect('google_form')


