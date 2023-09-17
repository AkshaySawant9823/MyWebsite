from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_func, name='twitterHome'),
    path('notification/', views.notification_func, name='twitterNotification'),
    path('profile/', views.profile_func, name='twitterProfile'),
    path('language/', views.language_func, name='twitterLanguage'),
]