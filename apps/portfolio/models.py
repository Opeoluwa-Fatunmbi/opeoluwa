from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel

# Create your models here.


class Project(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="project")
    url = models.URLField(_("URL"), max_length=200, blank=True, null=True)
    github_url = models.URLField(_("Github URL"), max_length=200, blank=True, null=True)
    medium_url = models.URLField(_("Medium URL"), max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name
