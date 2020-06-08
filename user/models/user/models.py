from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from .validators import CustomEmailValidator


class CustomUser(AbstractUser):

    username = None

    email = models.EmailField(
        _('email address'),
        null=True,
        blank=True,
        unique=True,
        validators=[CustomEmailValidator],
        help_text=_('Emails ending with socar-aqs.com are only accepted.'),
        error_messages={
            'unique': _("An user with that email already exists."),
        },
    )

    personal_number = models.IntegerField(
        unique=True,
    )

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['department', 'workplace']
    USERNAME_FIELD = 'personal_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return "Personal number: {0}".format(str(self.personal_number))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



