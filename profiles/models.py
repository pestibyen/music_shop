from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, default='', blank=True,
                             help_text='+375xxxxxxxxx',
                             validators=[validators.RegexValidator(regex='^\+[0-9]{12}$')])

    addresslist = models.CharField(verbose_name='Address',
                                   max_length=300, default='', blank=True,
                                   validators=[validators.int_list_validator(sep=',')])

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{}'.format(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
