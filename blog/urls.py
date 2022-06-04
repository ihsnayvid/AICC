from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserListView

urlpatterns = [
   path('blog/', PostListView.as_view(), name='blog-home'),
   path('blog/user/<str:username>', UserListView.as_view(), name='user_post'),
   path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('about/',views.about, name='blog-about'),
   path('blog/post/new/', PostCreateView.as_view(), name='post_create'),
   path('blog/post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
   path('blog/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
   path('search/',views.searchblog,name='search-blog'),
   path('comment/',views.add_comment,name='comments'),
  
   
] 