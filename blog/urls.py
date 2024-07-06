from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/create/', views.create_post, name='create_post'),  
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comments/', views.post_comments, name='post_comments'),
]
