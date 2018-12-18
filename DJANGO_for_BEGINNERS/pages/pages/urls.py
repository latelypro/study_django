from django.urls import path

from .views import HomePageView # View Classのimport

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # これでサーバー接続時にViewClassで指定したtemplateが表示されるようになる
]