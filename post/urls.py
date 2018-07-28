from django.urls import path, include
from . import views 
urlpatterns = [
    path('',views.home, name='home'),
    path('post/<int:pk>/',views.show_topics, name='show_topics'),
    path('post/new/', views.post_topics, name='post_topics'),
]    