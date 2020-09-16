# coding:utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse, get_object_or_404
from app.libs.base_render import render_to_response
from app.models import Video, Comment
from app.utils.permission import client_auth
from app.model.video import FromType, VideoType


class ExVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.exclude(from_to=FromType.custom.value)
        # videos = Video.objects.filter(video_type=VideoType.news.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)

class Movie(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.filter(video_type=VideoType.movie.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)

class Episode(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.filter(video_type=VideoType.episode.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)

class News(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.filter(video_type=VideoType.news.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)

class Variety(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.filter(video_type=VideoType.variety.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)

class CusVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.filter(from_to=FromType.custom.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)


class VideoSub(View):
    TEMPLATE = 'client/video/video_sub.html'

    def get(self, request, video_id):
        video = get_object_or_404(Video, pk=video_id)
        user = client_auth(request)

        comments = Comment.objects.filter(video=video, status=True).order_by('-id')

        data = {'video': video, 'user': user, 'comments': comments}

        return render_to_response(request, self.TEMPLATE, data=data)
