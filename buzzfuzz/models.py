from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    random = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('buzzfuzz:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.user.username

    def delete(self):
        user = self.user
        super(Profile, self).delete()
        user.delete()

    # def save(self, *args, **kwargs):
    #     self.random = randint(0, 100)
    #     super(Profile, self).save(*args, **kwargs)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

