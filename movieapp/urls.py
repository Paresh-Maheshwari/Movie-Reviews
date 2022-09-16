
from django.contrib import admin
from django.urls import path,include
from movie import views
from django.conf.urls.static import static,serve
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.About,name='about'),
    path('signup/',views.signup,name='signup'),
    path('news/',include('news.urls')),
    path('movie/', include('movie.urls')),
    path('accounts/',include('accounts.urls')),


    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]


urlpatterns +=static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)