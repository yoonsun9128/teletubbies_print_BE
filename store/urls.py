from django.urls import path
from store import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store_view'), #필터리스트 메인페이지
    path('<int:filter_id>/', views.OptionSettingPageView.as_view(), name='option_setting_page_view'), # 구매옵션설정페이지
    path('<int:filter_id>/', views.ReviewView.as_view(), name='comment_view'), #fetch를 보낼 때 같이보내면 된다?
    path('<int:filter_id>/order/', views.OrderPageView.as_view(), name='order_page_view') #구매페이지
]
