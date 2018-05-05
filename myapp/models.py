from django.db import models


class Episode(models.Model):

    name = models.CharField('お名前', max_length=255)
    ken = models.CharField('都道府県', max_length=255, blank=True)
    episode = models.TextField('エピソード', blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    
    def __str__(self):
        return self.name




