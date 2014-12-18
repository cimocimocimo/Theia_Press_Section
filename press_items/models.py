from django.db import models
from uuslug import uuslug
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField

# Create your models here.

class PressItemType(models.Model):
    name = models.TextField(max_length=64)    
    slug = models.SlugField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class PressItem(models.Model):
    # **TODO** add type field for filtering

    slug_max_length = 256

    title = models.TextField(max_length=256)
    slug = models.SlugField(max_length=slug_max_length, unique=True)
    organization_name = models.TextField(max_length=256)
    url = models.URLField(max_length=512)
    original_publication_date = models.DateField()
    published_date = models.DateField()
    content = PlaceholderField('press_item_content')
    item_type = models.ForeignKey(PressItemType)

    # **TODO** Add django-taggit

    def __unicode__(self):
        return self.title

    # **TODO** auto generate the slug from the title so that the user doesn't have to add in a default value for slug
    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, start_no=2, max_length=self.__class__.slug_max_length)
        super(PressItem, self).save(*args, **kwargs)



