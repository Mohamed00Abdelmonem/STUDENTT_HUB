from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'teacher'

urlpatterns = [

                  path('contents', views.contents, name='contents'),
                  path('base_nav', views.base_nav, name='base_nav'),
                  # path('control_panel', control_panel, name='control_panel'),


                  path('control panel', views.control_panel, name='control_panel'),
                  path('contents_teacher', views.contents_teacher, name='contents_teacher'),
                  # path('exam', views.exam, name='exam'),
                  path('index', views.index, name='index'),
                  path('subject_form', views.subject_form, name='subject_form'),
                  path('lesson_form', views.lesson_form, name='lesson_form'),
                  path('exam_google', views.exam_google, name='exam_google'),
                  # path('subject', views.subjecte_List.as_view(), name='subject'),

                  path('subject', views.subject, name='subject'),
                  path('subject/<int:pk>', views.subject_detail.as_view(), name='subject_detail'),
                  path('lesson_list/<int:pk>', views.Lesson_Detail.as_view(), name='lesson_detail'),



              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)