from django.urls import path
#from . import views
from .views import HomeView, ArticleDetail, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', EditPostView.as_view(), name='edit_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]

