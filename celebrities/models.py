from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField

class Celebrity(models.Model):
    name = models.TextField(max_length=256)
    content = PlaceholderField('celebrity_content')
    # tags?

    slug_max_length = 256
    slug = models.SlugField(max_length=slug_max_length, unique=True)

    def __unicode__(self):
        return self.name


class Dress(models.Model):
    title = models.TextField(max_length=256)
    # event dress worn at?
    celebrity = models.ForeignKey(Celebrity)
    content = PlaceholderField('celebrity_content')
    # tags?
    # link to dress product page

    slug_max_length = 256
    slug = models.SlugField(max_length=slug_max_length, unique=True)

    def __unicode__(self):
        return self.title
