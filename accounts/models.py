from django.db import models
from django.contrib.auth.models import User
# Create your models here.


job_type = (
    ('Choose Job Type', 'Choose Job Type'),
    ('Marketer', 'Marketer'),
    ('Seller', 'Seller'),
)


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=False)
    image = models.ImageField(default='avatar.png', upload_to='profile_images', null=True, blank=False)
    job_type = models.CharField(max_length=150, choices=job_type, null=False, blank=False)

    def __str__(self):
        return f"{self.staff} -- {self.job_type}"

