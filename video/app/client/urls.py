# coding:utf-8

from django.urls import path
from .views.base import Index
from .views.video import ExVideo, Movie, Episode, News, Variety, CusVideo, VideoSub
from .views.auth import User, Regist, Logout
from .views.comment import CommentView


urlpatterns = [
  path('', Index.as_view(), name='client_index'),
  path('video/ex', ExVideo.as_view(), name='client_ex_video'),
  path('video/movie', Movie.as_view(), name='client_movie_video'),
  path('video/episode', Episode.as_view(), name='client_ep_video'),
  path('video/news', News.as_view(), name='client_news_video'),
  path('video/variety', Variety.as_view(), name='client_variety_video'),
  path('video/custom', CusVideo.as_view(), name='client_cus_video'),
  path('video/<int:video_id>', VideoSub.as_view(), name='client_video_sub'),
  path('auth', User.as_view(), name='client_auth'),
  path('auth/regist', Regist.as_view(), name='client_regist'),
  path('auth/logout', Logout.as_view(), name='client_logout'),
  path('comment/add', CommentView.as_view(), name='client_add_comment')
]
