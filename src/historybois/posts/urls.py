from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # CREATE
    path("p/new/", views.PostCreate.as_view(), name='post_create'),

    # READ
    path("", views.PostList.as_view(), name='post_list'),
    path("p/<str:pk>/", views.PostDetail.as_view(), name='post_detail'),

    # UPDATE
    path("p/<str:pk>/update/", views.PostUpdate.as_view(), name='post_update'),

    # DELETE
    path("p/<str:pk>/delete/", views.PostDelete.as_view(), name='post_delete')
]
