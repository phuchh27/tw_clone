
from django.contrib import admin
from django.urls import path ,re_path


from tweets.views import home_views , tweet_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views),
    path('tweet/<int:tweet_id>', tweet_detail_view),
]
