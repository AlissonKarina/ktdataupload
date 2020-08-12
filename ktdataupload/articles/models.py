from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treatment(models.Model):
    treatment = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    #contexts, 
    class Meta:
        ordering = ["treatment"]
    
    def __str__(self):
        return str(self.id) + "-" + self.treatment

class Article (models.Model):
    title = models.CharField(max_length = 400)
    author = models.CharField(max_length = 400)
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='articles', null=True, blank = True)
    processed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #contexts
    idUser = models.ForeignKey(User, db_column='idUser', default=1, related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.id) + "-" + self.title

class Context (models.Model):
    context = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #questions
    idTreatment = models.ForeignKey(Treatment, db_column='idTreatment', related_name='contexts', on_delete=models.CASCADE)
    idArticle = models.ForeignKey(Article, db_column='idArticle', related_name='contexts', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + "-" + self.context

class Question (models.Model):
    question = models.TextField()
    answer = models.TextField(max_length = 500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    idContext = models.ForeignKey(Context, db_column='idContext', related_name='questions', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + "-" + self.question

