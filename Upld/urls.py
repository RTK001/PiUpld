from django.urls import path
from . import views

app_name = "Upld"

urlpatterns = [
path('', views.IndexView.as_view(), name = 'index'),
path('ProjectCreateView', views.ProjectCreateView.as_view(), name='ProjectCreateView'),
path('ClassStream', views.StreamingTest.as_view(), name = 'ClassStream'),
]
