from django.db import models
from django.conf import settings

class TicketType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TicketStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TicketPriority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TicketCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  # No rich text, just a simple TextField
    type = models.ForeignKey(TicketType, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(TicketStatus, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(TicketPriority, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(TicketCategory, on_delete=models.SET_NULL, null=True)

    # Relationships
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='submitted_tickets', on_delete=models.CASCADE)
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_tickets', on_delete=models.SET_NULL, null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id}: {self.title}"