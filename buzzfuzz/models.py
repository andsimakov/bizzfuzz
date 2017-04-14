from random import randint
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    random = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('buzzfuzz:detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        self.random = randint(0, 100)
        super(Profile, self).save(*args, **kwargs)
