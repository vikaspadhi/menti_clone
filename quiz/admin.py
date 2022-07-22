from django.contrib import admin
from .models import Menti,Player,Question,Answer
import nested_admin

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id','username','room','score']

admin.site.register(Player,PlayerAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display=['id','answer','is_correct']

# admin.site.register(Answer,AnswerAdmin)

class AnswerInline(nested_admin.NestedTabularInline):
    model= Answer
    extra = 0

class QuestionInline(nested_admin.NestedTabularInline):
    model=Question
    extra = 0
    inlines =[AnswerInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display=['id','question','room']
    inlines= [AnswerInline]

# admin.site.register(Question,QuestionAdmin)


class MentiAdmin(nested_admin.NestedModelAdmin):
    list_display = ['id','room','users_joined','status']
    list_editable=['status']
    # readonly_fields=('users_joined',)
    search_fields= ['room']
    inlines=[QuestionInline,]
    

admin.site.register(Menti,MentiAdmin)

