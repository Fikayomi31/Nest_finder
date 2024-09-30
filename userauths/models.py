from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    """Creating a user class"""
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    otp = models.CharField(unique= True, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """str reoresentation of the class User"""
        return self.email

    def save(self, *args, **kwargs):
        email_username, full_name = self.email.split('@')
        if self.full_name == "" or self.full_name == None:
            self.full_name == self.username

        if self.username == "" or self.username == None:
            self.username = email_username
        super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    """Creating a Profile for the User class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_folder', default='default.jpg', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """str repreentation of the profile"""
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)


    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name == self.user.username
        super(Profile, self).save(*args, **kwargs)
        

def create_user_profile(sender, instance, created, **kwargs):
    """To create a User profile when a new User is be created or updated"""
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    """To save a User profile when a new User is be created or updated"""
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
