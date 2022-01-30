from django import forms

from tickets.models import Ticket, Review


class TicketForm(forms.ModelForm):
    """a form to handle the creation of Ticket objects"""
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    """a form to handle the creation of Review objects"""
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        CHOICES = [(i, f"- {i}") for i in range(6)]
        widgets = {
            'rating': forms.RadioSelect(choices=CHOICES)
            }
