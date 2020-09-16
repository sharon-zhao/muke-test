# coding:utf-8

from enum import Enum
from django.db import models


class VideoType(Enum):
    movie = 'movie'
    cartoon = 'cartoon'
    episode = 'episode'
    variety = 'variety'
    news = 'news'
    other = 'other'

VideoType.movie.label = 'Movie'
VideoType.cartoon.label = 'Cartoon'
VideoType.episode.label = 'Episode'
VideoType.variety.label = 'Variety'
VideoType.news.label = 'News'
VideoType.other.label = 'Other'


class FromType(Enum):
    youku = 'youku'
    youtube = 'youtube'
    custom = 'custom'
FromType.youku.label = 'youku'
FromType.youtube.label = 'youtube'
FromType.custom.label = 'custom'


class NationalityType(Enum):
    china = 'china'
    japan = 'japan'
    korea = 'korea'
    europe = 'europe'
    america = 'america'
    other = 'other'

NationalityType.america.label = 'America'
NationalityType.europe.label = 'Europe'
NationalityType.china.label = 'China'
NationalityType.japan.label = 'Japan'
NationalityType.korea.label = 'Korea'
NationalityType.other.label = 'other'

class IdentityType(Enum):
    lead_actor = 'lead_actor'
    supporting_rule = 'supporting_rule'
    director = 'director'

IdentityType.lead_actor.label = 'Lead Actor'
IdentityType.supporting_rule.label = 'Supporting Rule'
IdentityType.director.label = 'Director'


class Video(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.CharField(max_length=500, default='')
    video_type = models.CharField(max_length=50, default=VideoType.other.value)
    from_to = models.CharField(max_length=20, null=False, default=FromType.custom.value)
    nationality = models.CharField(max_length=20, default=NationalityType.other.value)
    info = models.TextField()
    status = models.BooleanField(default=True, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'video_type', 'from_to', 'nationality')

    def __str__(self):
        return self.name


class VideoStar(models.Model):
    video = models.ForeignKey(
        Video,
        related_name='video_star',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    name = models.CharField(max_length=100, null=False)
    identity = models.CharField(max_length=50, default='')

    class Meta:
        unique_together = ('video', 'name', 'identity')

    @property
    def ident(self):
        try:
            result = IdentityType(self.identity)
        except:
            return ''
        return result.label

    def __str__(self):
        return self.name


class VideoSub(models.Model):
    video = models.ForeignKey(
        Video,
        related_name='video_sub',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    url = models.CharField(max_length=500, null=False)
    number = models.IntegerField(default=1)

    class Meta:
        unique_together = ('video', 'number')

    def __str__(self):
        return 'video:{}, number:{}'.format(self.video.name, self.number)
