from django.contrib import admin

from .models import Task, TaskList, Attachment


class TaskListAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')
    

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')
    

class AttachmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Attachment, AttachmentAdmin)
