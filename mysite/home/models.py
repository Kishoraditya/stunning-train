from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    template = 'home/home_page.html'

    heading = models.CharField(max_length=255, default="Welcome to Our Website")
    sub_heading = models.CharField(max_length=255, default="Discover Amazing Content")
    button_text = models.CharField(max_length=50, default="Learn More")
    button_link = models.URLField(default="https://example.com")

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        FieldPanel('button_text'),
        FieldPanel('button_link'),
    ]