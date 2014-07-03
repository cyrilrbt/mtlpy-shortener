from django.contrib import admin
from mtlpy.shortener.models import Shortcut


class ShortcutAdmin(admin.ModelAdmin):
    list_display = ('slug', 'link')

admin.site.register(Shortcut, ShortcutAdmin)
