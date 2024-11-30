from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# url paths to the view functions 
urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.post_list, name='blog'),
    path('blog/<int:pk>/', views.blog_details, name='blog_details'),
    path('project', views.projects, name='projects'),
    path('project/<int:pk>/', views.project_details, name='project_details'),
    path('achievments', views.achievments, name='achievments'),
    path('contect', views.contect, name='contect'),
    path('gallery', views.gallery, name='gallery'),
    path('cv/', views.cv, name='cv'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]