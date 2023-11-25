from django.db import models
from django.contrib.auth.models import User

from core.models import Phones
# Create your models here.





phns = Phones.objects.all()

phns_list = []
for c in phns:
    phns_list.append((str(c), str(c)))

phns_tuple = tuple(phns_list)




class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    image = models.ImageField(default='avatar.png', upload_to='profile_images', null=True)
    # phones = field_one = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return f'{self.staff.username} profile'