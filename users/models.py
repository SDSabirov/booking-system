from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.models import TimeStamp

class User(AbstractUser):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('employee', 'Employee'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    business = models.ForeignKey('Business', on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions', 
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Business(TimeStamp):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owned_business')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    logo = models.ImageField(blank = True, null=True, upload_to="logos")
    website_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='employees')
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.name} - {self.designation}"

