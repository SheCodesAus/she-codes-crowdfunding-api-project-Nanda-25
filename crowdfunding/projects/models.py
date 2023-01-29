from django.contrib.auth import get_user_model
from django.db import models
from users.models import CustomUser

User = get_user_model()

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='owner_projects'
        )
bookmarked_by = models.ManyToManyField(CustomUser, related_name='bookmarked_projects')

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="pledges")
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )