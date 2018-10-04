from .views import (
    TweetDetailView,
    TweetListView,
    TweetCreateView
)
from django.conf.urls import url

urlpatterns = [
    # dollar means the end of URL
    url(r'^$', TweetListView.as_view(), name="list"), #tweet
    url(r'^create/$', TweetCreateView.as_view(), name="create"), #tweet/create
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail"), #tweet/<pk>
]

