from django.contrib import admin

from .models import Article, Context, Question, Treatment

# Register your models here.
""" class TreatmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'treatment')
    list_display = ('id', 'treatment')
    ordering = ('treatment',)
    list_filter = ('treatment',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')
    list_display = ('id', 'author', 'title', 'year', 'processed')
    ordering = ('created', 'updated', 'year')
    #search_fields = ('title', 'author', 'user__username')
    date_hierarchy = 'updated'
    #list_filter = ('user__username',)

class ContextAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')
    #list_display = ('id', 'context', 'article__title')
    ordering = ('created', 'updated')
    #search_fields = ('context', 'treatment__treatment', 'article__title')
    list_filter = ('treatment__treatment',)

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created', 'updated')
    #list_display = ('id','question','answer', 'context_context')
    ordering = ('created', 'updated')
    search_fields = ('question', 'answer')
    #list_filter = ('context_context', 'context_treatment__treatment') """

admin.site.register(Article)
admin.site.register(Context)
admin.site.register(Question)
admin.site.register(Treatment)
