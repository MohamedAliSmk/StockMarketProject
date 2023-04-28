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
    # add additional fields as needed

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Convert the Django model instance to a dictionary
        user_dict = {
            'username': self.user.username,
            'email': self.user.email,
            'lastName': self.user.lastName,
            'country': self.user.country,
            'dateOfBirth': self.user.dateOfBirth,
            'jobTitle': self.user.jobTitle,
            'yearsOfExperience': self.user.yearsOfExperience,
            'paymentMethod': self.user.paymentMethod,
            'subscription': self.user.subscription,
            'photo': self.user.photo, 
            'points': self.user.points,
            'phoneNumber': self.user.phoneNumber,
            'skills': [self.user.skills],
            'latestActivities': [self.user.latestActivities],
            'bio': self.user.bio,
            'socialLinks': {
                'twitter': self.user.twitter,
                'facebook': self.user.facebook,
                'linkedin': self.user.linkedin,
                'youtube': self.user.youtube
            },
            'portfolio': [self.user.portfolio] 
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