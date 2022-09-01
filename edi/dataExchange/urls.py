from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('handle_xml_upload/', views.handle_xml_upload, name='handle_xml_upload'),
]