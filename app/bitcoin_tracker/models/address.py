from django.db import models

__all__ = ['Address']


class Address(models.Model):
    data = models.CharField(
        help_text="Bitcoin public key",
        unique=True,
        max_length=100,
        validators=[]
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )
    date_modified = models.DateTimeField(
        auto_now_add=True,
    )
    label = models.CharField(
        help_text="Descriptive text to associate with the public key.",
        default="",
        blank=True,
        max_length=100,
    )

    def __str__(self):
        return str(self.data)
