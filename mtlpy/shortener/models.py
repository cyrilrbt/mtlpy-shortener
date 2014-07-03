import string
from random import choice

from django.db import models
from django.conf import settings


class Shortcut(models.Model):
    slug = models.CharField(max_length = 10, primary_key = True, editable=False)
    link = models.URLField(verify_exists = False)

    def make_slug(self, len):
        rc = ""

        b64_chars = string.ascii_letters + string.digits + "_-"
        for i in range(len):
            rc += choice(b64_chars)

        return rc

    def short_link(self):
        return "%s%s" % (settings.BASE_URL, self.slug)

    def save(self, *args, **kwargs):
        exist = Shortcut.objects.filter(link = self.link)
        if len(exist) == 0:
            if self.slug is None or len(self.slug) == 0:
                success = False
                for offset in range(3):
                    for attempt in range(5):
                        self.slug = self.make_slug(settings.MIN_LENGTH+offset)
                        try:
                            super(Shortcut, self).save(*args, **kwargs)
                            success = True
                        except:
                            pass
                        if success:
                            break
                    if success:
                        break
