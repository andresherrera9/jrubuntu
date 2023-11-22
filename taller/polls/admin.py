from django.contrib import admin
from .models import Quizros,Cuest,answ



class QuizrosAdmin(admin.ModelAdmin):
    model = Quizros

class CuestAdmin(admin.ModelAdmin):
    list_display = ('question','quizros')
    list_filter = ['quizros']


class answAdmin(admin.ModelAdmin):
    model = answ
    list_display = ('text','question')
    list_filter = ['question']
    
    


admin.site.register(Quizros)
admin.site.register(Cuest,CuestAdmin)
admin.site.register(answ,answAdmin)













#class CuestAdmin(admin.ModelAdmin):
#    list_display = ('question','quizros')
#    list_filter = ['quizros']


#class CuestInline(admin.TabularInline):
#    model = Cuest
#    extra = 1

#class AnswInline(admin.TabularInline):
#    model = answ
#    extra = 2
#    list_filter = ['question']
    

#class QuizrosAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Numero ROS',          {'fields': ['nombre']}),
#        ('Numero de preguntas',{'fields': ['num_preguntas'], 'classes': ['collapse']}),
        
#    ]
#    inlines=[CuestInline,AnswInline]
    #list_filter = ['question']
    


#admin.site.register(Quizros,QuizrosAdmin)



