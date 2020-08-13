from django.urls import path

from .views import ArticleAPI, ReviewAPI, TreatmentAPI

urlpatterns = [
    path('treatment/', TreatmentAPI.as_view(), name = "api_list_treatment"),

    path('', ArticleAPI.as_view(), name = "api_create_article"),
    path('list/<int:idUser>/', ArticleAPI.as_view(), name = "api_list_article"),
    path('<int:idArticle>/', ArticleAPI.as_view(), name = "api_update_article"),
    path('review/', ReviewAPI.as_view(), name = "api_review_article"),
    path('delete/<int:idArticle>/', ArticleAPI.as_view(), name = "api_delete_article"),
]