from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = "Polling Admin"
admin.site.site_title = "Polling Admin Area"
admin.site.index_title = "Welcome to Polling Admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0 # extra fields after choices


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ] # 1. we are setting up the question here question text -> its a collapsable date info
                 # and the inlines are the items.
    inlines = [ChoiceInline] # this brings in the array of choices from the model.


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin) # we are combining choices and question here in admin as they are related.
