from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article, Context, Question, Treatment

class QuestionSerializer(serializers.Serializer):
    idQuestion = serializers.ReadOnlyField(source='id')
    question = serializers.CharField()
    answer = serializers.CharField()
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
    # Read only
    idContext = serializers.ReadOnlyField(source='id')
    treatment = serializers.SlugRelatedField(
        source='idTreatment',
        many=False, 
        read_only=True, 
        slug_field='treatment'
    ) 
    
    # Write only
    #idArticle = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Article.objects.all())
    idTreatment = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Treatment.objects.all())
    
    # Read Write
    context = serializers.CharField()
    questions = QuestionSerializer(many=True)
    
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

class ArticleUpdateSerializer(serializers.ModelSerializer):
    contexts = ContextSerializer(many=True)
    class Meta:
        model = Article
        fields = (
            'id', 'title', 'author', 'year',
            'description', 'contexts',    
        )
        depth = 1
    
    def update(self, instance, data):
        instance.title = data.get('title')
        instance.author = data.get('author')
        instance.year = data.get('year')
        instance.description = data.get('description')
        instance.save()
        contexts_data = data.pop('contexts')
        for context_data in contexts_data:
            context = Context.objects.create(
                idTreatment=context_data.get('idTreatment'),
                idArticle=instance,
                context=context_data.get('context')
            )
            questions_data = context_data.pop('questions')
            for question_data in questions_data:
                Question.objects.create(
                    idContext=context,
                    question=question_data.get('question'),
                    answer=question_data.get('answer')
                )
        return instance

class ArticleListSerializer(serializers.ModelSerializer):
    reviewer = serializers.SlugRelatedField(
        source='idUser',
        many=False, 
        read_only=True, 
        slug_field='username'
    )
    urlArticle = serializers.ImageField(read_only=True, source='file')
    contexts = ContextSerializer(many=True)
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

class ArticleReviewSerializer(serializers.ModelSerializer):
    idArticle = serializers.ReadOnlyField(source='id')
    idUser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    contexts = ContextSerializer(many=True)
    class Meta:
        model = Article
        fields = (
            'idUser', 'idArticle', 'contexts', 
        )
        depth = 1
    
    def update(self, instance, data):
        instance.processed = 1
        instance.save()
        contexts_data = data.pop('contexts')
        for context_data in contexts_data:
            context = Context.objects.create(
                idTreatment=context_data.get('idTreatment'),
                idArticle=instance,
                context=context_data.get('context')
            )
            questions_data = context_data.pop('questions')
            for question_data in questions_data:
                Question.objects.create(
                    idContext=context,
                    question=question_data.get('question'),
                    answer=question_data.get('answer')
                )
        return instance


