from django.contrib import admin
from .models import Resume

# admin.site.register(Resume)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'uploaded_at')
    list_filter = ('uploaded_at', 'user')
    search_fields = ('user__username', 'file')

