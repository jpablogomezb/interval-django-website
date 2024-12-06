from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.models import Image



class HomePage(Page):
    header = models.CharField(max_length=125, default="Project name")
    section_1_title = models.CharField(max_length=125, default="Section title")
    section_1_text = models.CharField(max_length=500, default="Section text")
    section_1_call_to_action = models.CharField(
        max_length=50, blank=True, null=True)
    section_1_call_to_action_path = models.CharField(
        max_length=25, blank=True, null=True)
    tile_1_header = models.CharField(max_length=150, default="Tile 1 header")
    tile_2_header = models.CharField(max_length=150, default="Tile 2 header")
    tile_3_header = models.CharField(max_length=150, default="Tile 3 header")
    tile_4_header = models.CharField(max_length=150, default="Tile 4 header")
    tile_5_header = models.CharField(max_length=150, default="Tile 5 header")
    tiles_call_to_action = models.CharField(
        max_length=50, blank=True, null=True)
    tiles_call_to_action_path = models.CharField(
        max_length=25, blank=True, null=True)
    blockquote_text = models.CharField(
        max_length=250, default="Project blockquote")

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('section_1_title'),
        FieldPanel('section_1_text'),
        FieldPanel('section_1_call_to_action'),
        FieldPanel('section_1_call_to_action_path'),
        FieldPanel('tile_1_header'),
        FieldPanel('tile_2_header'),
        FieldPanel('tile_3_header'),
        FieldPanel('tile_4_header'),
        FieldPanel('tile_5_header'),
        FieldPanel('tiles_call_to_action'),
        FieldPanel('tiles_call_to_action_path'),
        FieldPanel('blockquote_text'),
    ]


class LandingPage(Page):
    subtitle = models.CharField(max_length=125)
    section_1_title = models.CharField(max_length=250)
    section_1_desc = RichTextField()
    section_1_call_to_action = models.CharField(
        max_length=50, blank=True, null=True)
    section_1_call_to_action_path = models.CharField(
        max_length=25, blank=True, null=True)
    section_2_title = models.CharField(max_length=250)
    section_2_desc = RichTextField()
    section_2_call_to_action = models.CharField(
        max_length=50, blank=True, null=True)
    section_2_call_to_action_path = models.CharField(
        max_length=25, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('section_1_title'),
        FieldPanel('section_1_desc'),
        FieldPanel('section_1_call_to_action'),
        FieldPanel('section_1_call_to_action_path'),
        FieldPanel('section_2_title'),
        FieldPanel('section_2_desc'),
        FieldPanel('section_2_call_to_action'),
        FieldPanel('section_2_call_to_action_path'),
    ]



class WorkshopPage(Page):
    # Section 1: Workshop Overview
    desc = models.CharField(max_length=250, blank=True, null=True, help_text="Short description or tagline for the workshop.")
    description = RichTextField(blank=True, null=True, help_text="Detailed description of the workshop.")

    # Section 2: Highlights of the Workshop
    highlight_title = models.CharField(max_length=150, blank=True, null=True, help_text="Title for the highlights section.")
    highlight_images = models.ManyToManyField(
        Image,
        blank=True,
        help_text="Upload multiple images to create a collage for the highlights.",
    )

    # Section 3: Key Takeaways
    takeaways_title = models.CharField(max_length=150, blank=True, null=True, help_text="Title for the key takeaways section.")
    takeaways = RichTextField(blank=True, null=True, help_text="Key points or takeaways from the workshop.")

    # Section 4: Feedback or Testimonials
    feedback_title = models.CharField(max_length=150, blank=True, null=True, help_text="Title for the feedback section.")
    feedback = RichTextField(blank=True, null=True, help_text="Add feedback or testimonials from workshop participants.")

    content_panels = Page.content_panels + [
        FieldPanel('desc'),
        FieldPanel('description'),
        MultiFieldPanel([
            FieldPanel('highlight_title'),
            FieldPanel('highlight_images'),
        ], heading="Workshop Highlights"),
        MultiFieldPanel([
            FieldPanel('takeaways_title'),
            FieldPanel('takeaways'),
        ], heading="Key Takeaways"),
        MultiFieldPanel([
            FieldPanel('feedback_title'),
            FieldPanel('feedback'),
        ], heading="Feedback and Testimonials"),
    ]