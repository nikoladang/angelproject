from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from blog.models import PostPage


class HomePage(Page):
    body = RichTextField(blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def post_pages(self):
        # print("xzxxx")
        # print(PostPage.objects.all())
        return PostPage.objects.live()

    # def get_context(self, request, *args, **kwargs):
    #     context = super(PostPage, self).get_context(request)
    #     context['post_pages'] = self.get_children().type(PostPage)
    #     return context