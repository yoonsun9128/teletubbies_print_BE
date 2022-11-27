from django.urls import path
from store import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store_view'), #필터리스트 메인페이지
    path('<int:filter_id>/', views.UploadImageView.as_view(), name='upload_image_view'),
    path('articles/', views.ArticleView.as_view(), name='article_view'), # 게시글리스트페이지
    path('articles/<int:image_id>/', views.ArticleDetailView.as_view(), name='article_detail_view'), # 게시글상세페이지
]
