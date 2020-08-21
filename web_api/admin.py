from django.contrib import admin
from .models import NowPlaying

class NowPlayingAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'time_on_air', 'lyrics')

# Register your models here.
admin.site.register(NowPlaying, NowPlayingAdmin)
