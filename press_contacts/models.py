from django.db import models

from cms.models import CMSPlugin

# Create your models here.
class PressContact(models.Model):
    descriptive_text = models.CharField(max_length=2048)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=64)


class PressContactPluginModel(CMSPlugin):
    press_contact = models.ForeignKey('press_contacts.PressContact', related_name='plugins')

    
