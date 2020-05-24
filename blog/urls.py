from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(),name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/$', views.PostDetails.as_view(), name='details'),
    path('post/new/$',views.CreatePostView.as_view(),name='post_name'),
    path('post/new/$',views.CreatePostView.as_view(),name='post_name'),
    path('post/<int:pk>/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/$', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/',views.DraftListView.as_view(),name='draft_post'),
    path('post/<int:pk>/comment/$', views.add_cooment, name='add_comment'),
    path('comment/<int:pk>/approve/$', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/$', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/$', views.post_publish, name='post_publish'),
]
