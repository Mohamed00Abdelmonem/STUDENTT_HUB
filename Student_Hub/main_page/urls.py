from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('', views.home, name='home'),
                  path('signin', views.signin, name='signin'),
                  path('how_to_make_website', views.how_to_make_website, name='how_to_make_website'),
                  path('signin_teacher', views.signin_teacher, name='signin_teacher'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)