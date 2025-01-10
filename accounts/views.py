import os
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests


@csrf_exempt
def sign_in(request):
    return render(request, 'sign_in.html')


@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)

    # Extract user information
    email = user_data.get('email')
    given_name = user_data.get('given_name')
    family_name = user_data.get('family_name')
    picture = user_data.get('picture')

    # Check if user already exists
    user, created = User.objects.get_or_create(
        username=email,
        defaults={
            'first_name': given_name,
            'last_name': family_name,
            'email': email,
        }
    )

    if created:
        # You might also want to handle user profile creation here
        pass

    # Log the user in
    login(request, user)

    # Set user data in session
    request.session['user_data'] = {
        'email': email,
        'given_name': given_name,
        'picture': picture,
    }

    # Redirect to the originally requested page or /playlists/playlist_add/ if 'next' is not provided
    return redirect(request.GET.get('next', '/playlist/playlist_add/'))


def sign_out(request):
    # Clear the user data from the session
    request.session.pop('user_data', None)

    # Log the user out of the Django session
    logout(request)

    # Redirect to the login page or home page
    return redirect('sign_in')

