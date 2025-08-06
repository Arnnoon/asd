from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blogs/create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<str:uuid>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<str:uuid>/update/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blogs/<str:uuid>/comment/', views.CommentCreateView.as_view(), name='comment-create'),
    path('blogs/<str:uuid>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),
]
