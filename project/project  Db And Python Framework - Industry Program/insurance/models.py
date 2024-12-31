from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class PolicyHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)  # Status of approval

    def __str__(self):
        return f'{self.user.username} - {self.policy_type}'

