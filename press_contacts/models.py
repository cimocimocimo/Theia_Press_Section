from django.db import models

from cms.models import CMSPlugin

# Create your models here.
class PressContact(models.Model):
    descriptive_text = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class PressContactPluginModel(CMSPlugin):
    press_contact = models.ForeignKey('press_contacts.PressContact', related_name='plugins')

    
