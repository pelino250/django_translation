from django.db import models
from django.utils.translation import gettext as _


class Blog(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title
