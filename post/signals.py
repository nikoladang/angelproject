__author__ = 'nikoladang'
from wagtail.wagtailcore.signals import page_published
from .models import PostPage

def receiver(sender, **kwargs):
    pass

page_published.connect(receiver, sender=PostPage)