from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone



class CustomUser(AbstractUser):
    # Add additional fields if needed
    # Add related_name to prevent clashes with default auth.User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change the related name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change the related name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

User = get_user_model()

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50, default="Basic Plan")
    price = models.FloatField(default=9.99)
    description = models.TextField(default="A basic subscription plan")

    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"
    
class FeatureFlag(models.Model):
    name = models.CharField(max_length=100, default="New Feature")
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
