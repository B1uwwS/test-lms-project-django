from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home/', views.home, name="home"),
    path('youtube/', views.youtube, name="youtube"),
    path('datetime/', views.time, name="datetime"),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('post/', views.post_view, name='post'),
    path('add-post/', views.add_post, name='add-post'),


    # path('random/ ' рандлмное число)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

