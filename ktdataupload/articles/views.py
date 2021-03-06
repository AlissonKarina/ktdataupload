from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import (ArticleListSerializer, ArticleCreateSerializer, 
                          ArticleUpdateSerializer, ArticleReviewSerializer,
                          ContextSerializer, TreatmentListSerializer)
from .models import Article, Context, Treatment


# Create your views here.

class TreatmentAPI(APIView):
    def get(self, request):
        treatments = Treatment.objects.all()
        serializer = TreatmentListSerializer(treatments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
        
        # Eliminación de contexts
        Context.objects.filter(idArticle=idArticle).delete()

        # Serializer para modificar Article, actualización de contexts y questions
        serializer = ArticleUpdateSerializer(article, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"state": "Actualizado Exitosamente", "object":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idArticle):
        article = Article.objects.get(id=idArticle)
        article.delete()
        return Response({"state": "Eliminado Exitosamente"}, status=status.HTTP_204_NO_CONTENT)
    

class ReviewAPI(APIView):
    def post(self, request):
        article = Article.objects.get(id=request.data.get('idArticle'))
        serializer = ArticleReviewSerializer(article, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"state": "Revisado Exitosamente", "object":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        pass
