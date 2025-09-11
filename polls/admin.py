from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):   # Inline choices inside question
    model = Choice
    extra = 3   # show 3 empty choices by default

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # connect choices here
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
