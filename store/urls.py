from django.urls import path
from store import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store_view'), #필터리스트 메인페이지
    path('<int:filter_id>/', views.OptionSettingPageView.as_view(), name='option_setting_page_view'), # 구매옵션설정페이지
]
