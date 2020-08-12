from django.urls import path

from .views import ArticleAPI, ReviewAPI

urlpatterns = [
    path('article/', ArticleAPI.as_view(), name = "api_create_article"),
    path('article/list/<int:idUser>/', ArticleAPI.as_view(), name = "api_list_article"),
    path('article/<int:idArticle>/', ArticleAPI.as_view(), name = "api_update_article"),
    path('article/review/', ReviewAPI.as_view(), name = "api_review_article"),
    path('article/delete/<int:idArticle>/', ArticleAPI.as_view(), name = "api_delete_article"),
]