from django.db import models
from django.contrib.auth.models import User

class PolicyHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.policy_type}"
