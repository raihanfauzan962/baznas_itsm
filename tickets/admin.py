from django.contrib import admin
from .models import Ticket, TicketType, TicketStatus, TicketPriority, TicketCategory

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'status', 'priority', 'category', 'submitter', 'agent', 'created_at', 'updated_at')
    list_filter = ('type', 'status', 'priority', 'category')

admin.site.register(TicketType)
admin.site.register(TicketStatus)
admin.site.register(TicketPriority)
admin.site.register(TicketCategory)
