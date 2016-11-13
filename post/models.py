from datetime import datetime

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .constants import POSTPAGE_CATEGORIES

class PostIndexPage(Page):
    note = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('note', classname="full"),
    ]

    subpage_types = ['post.PostPage']

    def posts(self):
        # posts_index = PostIndexPage.objects.all().last()
        # print(posts_index.get_children())
        posts = PostPage.objects.live().descendant_of(self)
        posts = posts.order_by("-create_date")
        print(posts)
        return posts


    def post_paginator(self, pagenumber):
        posts = PostPage.objects.live().descendant_of(self)
        posts = posts.order_by("-create_date")
        paginator = Paginator(posts, 6)
        # pagin_posts = paginator.page(1)
        # print(pagin_posts)
        # if pagin_posts.has_previous():
        #     print("previous"))

        # if pagin_posts.has_next():
        #     print("next")

        try:
            pagination_posts = paginator.page(pagenumber)
        except PageNotAnInteger:
            pagination_posts = paginator.page(1)
        except EmptyPage:
            pagination_posts = paginator.page(paginator.num_pages)
        return pagination_posts


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        page = request.GET.get('page')
        print(page)
        paginated_posts = self.post_paginator(page)
        # print(self.title)
        # print(paginated_posts)
        context['paginated_posts'] = paginated_posts
        return context


class PostPage(Page):
    CATEGORIES = POSTPAGE_CATEGORIES

    post_cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    category = models.CharField(max_length=255, choices=CATEGORIES)
    # date = models.DateTimeField("Post date", default=datetime.now())
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    # hot = models.NullBooleanField(blank=True, null=True)
    hot = models.BooleanField(default=False)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('media', EmbedBlock())
    ])
    note = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('post_cover'),
        # FieldPanel('date'),
        FieldPanel('category'),
        FieldPanel('author'),
        FieldPanel('hot'),
        StreamFieldPanel('body'),
        FieldPanel('note', classname="full"),
    ]

    parent_page_types = ['post.PostIndexPage']

    api_fields = ('title', 'post_cover', 'create_date', 'author', 'hot','intro', 'body', 'note')

    def latest_posts(self):
        postindexpage = PostIndexPage.objects.all().last()
        # posts = PostPage.objects.live().descendant_of(postindexpage)
        posts = PostPage.objects.child_of(postindexpage).public().live()
        posts = posts.order_by("-create_date")
        posts = posts[:6]
        return posts


    def hottest_posts(self):
        posts = PostPage.objects.live().public().filter(hot=True)
        posts = posts.order_by("-create_date")
        posts = posts[:4]
        return posts


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        print(context)
        context['latest_posts'] = self.latest_posts()
        context['hottest_posts'] = self.hottest_posts()
        context['previous_post'] = self.get_prev_sibling()
        print(request.user)
        # print(self.get_next_sibling().url_path)
        # print(self.get_prev_sibling().url_path)
        return context
