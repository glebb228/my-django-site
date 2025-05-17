from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.QuestFeedBackView.as_view()),
    path('done/', views.result_func),
    path('secret/', views.AuthView.as_view()),
    path('show_info/', views.ListQuests.as_view()),
]
