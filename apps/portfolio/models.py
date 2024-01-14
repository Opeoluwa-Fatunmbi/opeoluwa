from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel

# Create your models here.


class Portfolio(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="portfolio")
    url = models.URLField(_("URL"), max_length=200, blank=True, null=True)
    github_url = models.URLField(_("Github URL"), max_length=200, blank=True, null=True)
    linkedin_url = models.URLField(
        _("Linkedin URL"), max_length=200, blank=True, null=True
    )
    twitter_url = models.URLField(
        _("Twitter URL"), max_length=200, blank=True, null=True
    )
    facebook_url = models.URLField(
        _("Facebook URL"), max_length=200, blank=True, null=True
    )
    instagram_url = models.URLField(
        _("Instagram URL"), max_length=200, blank=True, null=True
    )
    behance_url = models.URLField(
        _("Behance URL"), max_length=200, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

    def __str__(self):
        return self.name
