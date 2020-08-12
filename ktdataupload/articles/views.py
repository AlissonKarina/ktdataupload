from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import (ArticleListSerializer, ArticleCreateSerializer)
from .models import Article


# Create your views here.

class ArticleAPI(APIView):
    def get(self, request, idUser):
        processed, unprocessed = 1, 0
        articles = Article.objects.filter(idUser=idUser)

        article_unprocessed = articles.filter(processed = unprocessed)
        article_processed = articles.filter(processed = processed)
        article_all = Article.objects.filter(processed = processed).exclude(idUser=idUser)

        serializer_articles_unprocessed = ArticleListSerializer(article_unprocessed, many=True)
        serializer_articles_processed = ArticleListSerializer(article_processed, many=True)
        serializer_articles_all= ArticleListSerializer(article_all, many=True)
        
        response = {
            "unProcessed": serializer_articles_unprocessed.data,
            "processed": serializer_articles_processed.data,
            "allProcessed": serializer_articles_all.data
        }
        
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"state": "Creado Exitosamente", "object":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, idArticle):
        article = Article.objects.get(id=idArticle)
        serializer = ArticleCreateSerializer(article, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"state": "Actualizado Exitosamente", "object":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        return Response(serializer.data, status=status.HTTP_200_OK)
    
