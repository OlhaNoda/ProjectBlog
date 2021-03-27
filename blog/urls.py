from django.urls import path
from .views import HomeView, NewsView, NewsByCategoryView, NewsByTagView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:slug>/', NewsByCategoryView.as_view(), name='category'),
    path('news/<str:slug>/', NewsView.as_view(), name='news'),
    path('tag/<str:slug>/', NewsByTagView.as_view(), name='tag'),
]
