from django.urls import path
from . import views



urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('post/<str:pk>', views.post_detail, name='post_detail'), 
    path('update_post/<str:pk>', views.post_update, name='post_update'), 

    path("q/", views.post_search, name='search'),

    path("create_category/", views.create_category, name="create_category"),
    path("create_post/", views.create_post, name="create_post"),

    path("post_visibility/<str:pk>", views.post_visibility, name="post_visibility"),

    # path("blog/<slug>", PostDetailView.as_view(), name='post'),
 
]

