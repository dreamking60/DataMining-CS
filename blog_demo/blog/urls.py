from django.conf import settings
from django.contrib import admin
from django.urls import path
from blog.views import homepage, post, about, search, postlist, allposts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('postlist/<slug>/', postlist, name = 'postlist'),
    path('posts/', allposts, name = 'allposts'),
    path('search/', search, name = 'search'),
]
