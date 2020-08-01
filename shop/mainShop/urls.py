from django.urls import path

from mainShop import views


app_name = 'mainShop'
urlpatterns = [
    # path('', views.MenuView.as_view(), name='menu'),
    path('male/', views.MaleListView.as_view(), name='men'),
    path('female/', views.FemaleListView.as_view(), name='women'),
    path('return-policy/', views.ReturnAndExchangeView.as_view(), name='test'),

    path('<slug>', views.ModelFilteredListView.as_view(), name='detail'),
    path('<slug>/',
         views.shoes_detail_view,
         name='shoes'),
]
