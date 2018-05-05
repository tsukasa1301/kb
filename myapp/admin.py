from django.contrib import admin
from myapp.models import Episode



class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'ken','episode','created')
    fields = ('name', 'ken','episode')
    
admin.site.register(Episode, EpisodeAdmin)


