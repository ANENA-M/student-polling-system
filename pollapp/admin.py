from django.contrib import admin
from .models import Poll, PollResponse, EventPolls, school_opinion_poll
from .models import PollQuestion, PollOption
# admin login=> user:admin pass:1999

class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)


class PollResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'category', 'submitted_at')
    list_filter = ('category',)
    search_fields = ('question', 'answer')


class EventPollsAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'category', 'submitted_at')
    list_filter = ('category',)


class SchoolOpinionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'category', 'submitted_at')
    list_filter = ('category',)


class PollOptionInline(admin.TabularInline):
    model = PollOption
    extra = 3

class PollQuestionAdmin(admin.ModelAdmin):
    inlines = [PollOptionInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(PollResponse, PollResponseAdmin)
admin.site.register(EventPolls, EventPollsAdmin)
admin.site.register(school_opinion_poll, SchoolOpinionAdmin)
admin.site.register(PollQuestion, PollQuestionAdmin)