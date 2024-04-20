from django.urls import path
from .views import home, about, create_post_view, update_record_view, post_detail_view


urlpatterns = [
    path('', home, name="blog-home"),
    path('about/', about, name="blog-about"),
    
    path('create-post/', create_post_view, name="create-post"),
    path('update-post/', update_record_view, name="update-post"),
    path('post-detail/<int:pk>', post_detail_view, name="post-detail"),   
]