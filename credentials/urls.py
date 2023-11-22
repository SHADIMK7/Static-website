from django.conf.urls.static import static
from django.urls import path

from credentials import views
from travelproject1 import settings

urlpatterns = [
    path('register', views.register , name='register'),
    path('login' , views.login , name='login'),
    path('logout', views.logout, name='logout')
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                       document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                       document_root=settings.MEDIA_ROOT)