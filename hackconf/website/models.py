from __future__ import unicode_literals
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from wagtail.wagtaildocs.models import Document
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel


class HomePage(Page):
    # header section
    header_image_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    header_dates = models.CharField(max_length=255, blank=True, null=True)
    header_text = models.CharField(max_length=255, blank=True, null=True)
    # navigation section
    # about section
    video_id = models.CharField(max_length=255, blank=True, null=True)
    about_text = RichTextField(blank=True, null=True)
    # speakers section
    # TODO: add fields for this section

    # call for speakers section
    speakers_title = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    call_for_speakers_form_url = models.URLField(max_length=255, blank=True, null=True)
    call_for_speakers_description = RichTextField(blank=True, null=True)

    # sponsors section
    sponsors_text = RichTextField(blank=True, null=True)
    attendees_text = RichTextField(blank=True, null=True)
    streaming_text = RichTextField(blank=True, null=True)
    fb_text = RichTextField(blank=True, null=True)
    sponsors_partnership_description = RichTextField(blank=True, null=True)
    sponsors_partnership_document = footer_powered_by = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    # past events section

    # tickets section
    tickets_title = models.CharField(max_length=255, blank=True, null=True)
    tickets_description = RichTextField(blank=True, null=True)
    tickets_widget_code = models.TextField(blank=True, null=True)

    # location section
    location_title = models.CharField(max_length=255, blank=True, null=True)
    location_place = models.CharField(max_length=255, blank=True, null=True)
    location_contact = models.CharField(max_length=255, blank=True, null=True)
    location_time = models.CharField(max_length=255, blank=True, null=True)
    footer_organized_by = models.ForeignKey(
        'website.Partner',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    footer_powered_by = models.ForeignKey(
        'website.Partner',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('header_dates'),
        ImageChooserPanel('header_image_logo'),
        FieldPanel('header_text'),
        FieldPanel('video_id'),
        FieldPanel('about_text'),
        FieldPanel('speakers_title'),
        FieldPanel('call_for_speakers_form_url'),
        FieldPanel('call_for_speakers_description'),
        FieldPanel('sponsors_text'),
        FieldPanel('attendees_text'),
        FieldPanel('streaming_text'),
        FieldPanel('fb_text'),
        FieldPanel('sponsors_partnership_description'),
        DocumentChooserPanel('sponsors_partnership_document'),
        InlinePanel('general_partners', label="General Partners"),
        InlinePanel('media_partners', label="Media Partners"),
        InlinePanel('branch_partners', label="Branch Partners"),
        InlinePanel('past_events', label="Past Events"),
        FieldPanel('tickets_title'),
        FieldPanel('tickets_description'),
        FieldPanel('tickets_widget_code'),
        FieldPanel('location_title'),
        FieldPanel('location_place'),
        FieldPanel('location_contact'),
        FieldPanel('location_time'),
        SnippetChooserPanel('footer_organized_by'),
        InlinePanel('hosting_partners', label="Hosting Partners"),
        SnippetChooserPanel('footer_powered_by')
    ]


@register_snippet
class Partner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    website_url = models.URLField(max_length=255, blank=True, null=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
        FieldPanel('website_url'),
    ]

    def __str__(self):
        return self.name


class GeneralPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='general_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class MediaPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='media_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class BranchPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='branch_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class HostingPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='hosting_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


@register_snippet
class Event(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    video_id = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('video_id'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.name


class PastEvents(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='past_events')
    event = models.ForeignKey('website.Event', related_name='+')

    panels = [
        SnippetChooserPanel('event'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)
