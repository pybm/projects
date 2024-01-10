from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('myfirst.html', views.welcome, name='myfirst'),
    path('testing/', views.testing, name='testing'),  
    path('resume.html', views.resume, name='resume'),
    path('underconstruction.html', views.kyo, name='kyo'),
    path('projects.html', views.projects, name='projects'),
    path('detailsp.html', views.detailsp, name='detailsp'),
    path('projects/python/', views.detailsp, {'program': 'Python'}, name='detailsp_python'),
    path('projects/numpy/', views.detailsp, {'program': 'NumPy'}, name='detailsp_numpy'),
    path('projects/django/', views.detailsp, {'program': 'Django'}, name='detailsp_django'),
    
]
