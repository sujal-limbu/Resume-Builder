from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_resume, name='create_resume'),
    path('resume/<int:id>/', views.resume_detail, name='resume_detail'),
    path('resume/<int:id>/pdf/', views.download_pdf, name='download_pdf'),

]