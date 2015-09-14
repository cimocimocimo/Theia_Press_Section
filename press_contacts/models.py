from django.db import models

from cms.models import CMSPlugin

# Create your models here.
class PressContact(models.Model):
    descriptive_text = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    address = models.TextField(
        null=True,
        blank=True)
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    phone = models.CharField(
        max_length=64,
        null=True,
        blank=True)
    url = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    url_label = models.CharField(
        max_length=255,
        null=True,
        blank=True)

    def __str__(self):
        return self.name

class PressContactPluginModel(CMSPlugin):
    press_contact = models.ForeignKey('press_contacts.PressContact', related_name='plugins')

    
