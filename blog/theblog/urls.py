from django.urls import path
from . views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView,  AddCategoryView, LikeView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/delete',DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/',CategoryView, name="category"),
    path('like/<int:pk>/', LikeView, name="like_post")
]
