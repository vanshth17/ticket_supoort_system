from django.db import models
from django.contrib.auth.models import User

class TicketStatus(models.TextChoices):
    OPEN = 'OPEN' , 'Open'
    IN_PROGRESS = 'IN_PROGRESS' , 'In progress'
    RESOLVED = 'RESOLVED' , 'Resolved'
    CLOSED = 'CLOSED', 'Closed'

class Ticket(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices = TicketStatus.choices,
        default = TicketStatus.OPEN
    )

    created_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'created_tickets'
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'assigned_tickets'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
    

class Reply(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Reply by {self.author.username}"