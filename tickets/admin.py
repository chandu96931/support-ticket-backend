from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'priority', 'status', 'progress', 'created_at')
    list_filter = ('category', 'priority', 'status')
    search_fields = ('title', 'description')