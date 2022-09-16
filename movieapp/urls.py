
from django.contrib import admin
from django.urls import path,include
from movie import views
from django.conf.urls.static import static 
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.About,name='about'),
    path('signup/',views.signup,name='signup'),
    path('news/',include('news.urls')),
    path('movie/', include('movie.urls')),
    path('accounts/',include('accounts.urls')),

]


urlpatterns +=static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)