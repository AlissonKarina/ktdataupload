from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article, Context, Question, Treatment

class QuestionSerializer(serializers.Serializer):
    idQuestion = serializers.ReadOnlyField(source='id')
    question = serializers.ReadOnlyField()
    answer = serializers.ReadOnlyField()
    class Meta:
        model = Question
        fields = (
            'idQuestion', 'question', 'answer',
        )
    
    def create(self, data):
        instance = Question()
        instance.question = data.get('question')
        instance.answer = data.get('answer')
        instance.save()
        return instance
    

class ContextSerializer(serializers.Serializer):
    idContext = serializers.ReadOnlyField(source='id')
    context = serializers.CharField()
    #idArticle = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Article.objects.all())
    idTreatment = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Treatment.objects.all())
    treatment = serializers.SlugRelatedField(
        source='idTreatment',
        many=False, 
        read_only=True, 
        slug_field='treatment'
    ) 
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Context
        fields = (
            'idContext', 'context', 'treatment', 'questions'
        )
        depth = 1
    
    def create(self, data):
        instance = Context()
        instance.context = data.get('context')
        instance.idArticle = data.get('idArticle')
        instance.idTreatment = data.get('idTreatment')
        instance.save()
        return instance

    def update(self, instance, data):
        instance.context = data.get('context')
        instance.idTreatment = data.get('idTreatment')
        instance.save()
        return instance

class ArticleCreateSerializer(serializers.ModelSerializer):
    idUser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #contexts = ContextSerializer(many=True)
    class Meta:
        model = Article
        fields = (
            'title', 'author', 'year', 'file',
            'description', 'idUser',  
        )
    
    def create(self, data):
        instance = Article()
        instance.title = data.get('title')
        instance.author = data.get('author')
        instance.year = data.get('year')
        instance.file = data.get('file')
        instance.description = data.get('description')
        instance.idUser = data.get('idUser')
        instance.save()
        return instance

    def update(self, instance, data):
        instance.title = data.get('title')
        instance.author = data.get('author')
        instance.year = data.get('year')
        instance.description = data.get('description')
        instance.idUser = data.get('idUser')
        instance.save()

        contexts = Context.objects.filter(idArticle=instance.id)
        contexts.delete()
        contexts = ContextSerializer(data=instance.contexts)
        return instance

class ArticleListSerializer(serializers.ModelSerializer):
    reviewer = serializers.SlugRelatedField(
        source='idUser',
        many=False, 
        read_only=True, 
        slug_field='username'
    )
    urlArticle = serializers.ImageField(source='file')
    contexts = ContextSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = (
            'id', 'title', 'author', 'year', 'urlArticle',
            'description', 'reviewer', 'contexts',    
        )
        depth = 1
    
    def create(self, data):
        instance = Article()
        instance.title = data.get('title')
        instance.author = data.get('author')
        instance.year = data.get('year')
        instance.file = data.get('file')
        instance.description = data.get('description')
        instance.idUser = data.get('idUser')
        instance.save()
        return instance







class ArticleSerializer(serializers.ModelSerializer):
    idUser = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())
    reviewer = serializers.SlugRelatedField(
        source='idUser',
        many=False, 
        read_only=True, 
        slug_field='username'
    )
    urlArticle = serializers.ImageField(source='file')
    contexts = ContextSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = (
            'id', 'title', 'author', 'year', 'urlArticle',
            'description', 'idUser', 'reviewer', 'contexts',    
        )
        depth = 1
    
    def create(self, data):
        instance = Article()
        instance.title = data.get('title')
        instance.author = data.get('author')
        instance.year = data.get('year')
        instance.file = data.get('file')
        instance.description = data.get('description')
        instance.idUser = data.get('idUser')
        instance.save()
        return instance





