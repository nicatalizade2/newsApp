from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.index, name='news'),
    path('news/all', views.newsAll, name='news-all'),
    # path('news/view/<slug:new_slug>', views.details, name='view'),
]