from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Fintechers']
collection = db['users']

def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create new user
        user = User.objects.create_user(username, email, password)
        user.save()

        # Save user data to MongoDB
        collection.insert_one({
            'username': username,
            'email': email,
            'password': password
        })

        # Log in user and redirect to home page
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'sign_up.html')

def login(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Log in user and redirect to home page
            login(request, user)
            return redirect('/')
        else:
            # Show error message
            error = 'Invalid username or password'
            return render(request, 'sign_in.html', {'error': error})
    else:
        return render(request, 'sign_in.html')

def logout(request):
    # Log out user and redirect to login page
    logout(request)
    return redirect('/login/')

def profile(request):
    # Get user data from MongoDB
    user = collection.find_one({'username': request.user.username})

    if request.method == 'POST':
        # Update user data
        email = request.POST['email']
        password = request.POST['password']

        collection.update_one(
            {'username': request.user.username},
            {'$set': {'email': email, 'password': password}}
        )

        # Update user email in Django auth
        user.email = email
        user.save()

    return render(request, 'profile.html', {'user': user})
