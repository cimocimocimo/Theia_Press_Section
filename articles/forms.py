from django.forms import ModelForm
from .models import Article
from taggit_labels.widgets import LabelWidget
from taggit.forms import TagField

class ArticleForm(ModelForm):
    class Meta:
        mode = Article

    tags = TagField(required=False, widget=LabelWidget)
