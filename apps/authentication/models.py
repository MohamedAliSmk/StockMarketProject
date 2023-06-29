from django.db import models
from django.contrib.auth.models import User
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Fintechers']
user_collection = db['users']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    id = models.BigAutoField(primary_key=True)  # define a primary key field

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Convert the Django model instance to a dictionary
        user_dict = {
            'username': self.user.username,
            'email': self.user.email, 
                    }


        # Insert or update the document in the MongoDB collection
        user_collection.replace_one({'username': self.user.username}, user_dict, upsert=True)

        super(UserProfile, self).save(*args, **kwargs)

    @classmethod
    def load(cls, user):
        # Find the document in the MongoDB collection by username
        user_dict = user_collection.find_one({'username': user.username})

        # If the document exists, create a new UserProfile instance
        if user_dict:
            profile = cls(user=user, email=user_dict['email'])
            # set additional fields as needed
            return profile

        # If the document doesn't exist, return None
        return None
    
class UserProfileExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    jobTitle = models.CharField(max_length=255, blank=True)
    yearsOfExperience = models.IntegerField(blank=True, null=True)
    paymentMethod = models.CharField(max_length=255, blank=True)
    subscription = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='profile_photos', blank=True)
    points = models.IntegerField(default=0)
    phoneNumber = models.CharField(max_length=255, blank=True)
    skills = models.TextField(blank=True)
    latestActivities = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username




