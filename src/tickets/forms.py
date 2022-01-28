from django import forms

from tickets.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        CHOICES = [(i, f"- {i}") for i in range(6)]
        widgets = {
            'rating': forms.RadioSelect(choices=CHOICES)
            }
