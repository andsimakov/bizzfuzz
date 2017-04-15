from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    random = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('bizzfuzz:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.user.username

    def delete(self):
        user = self.user
        super(Profile, self).delete()
        user.delete()
