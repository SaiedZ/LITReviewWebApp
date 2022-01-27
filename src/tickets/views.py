from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from tickets import forms
from tickets.models import Ticket


@login_required
def home(request):
    context = {"user": request.user, 'nbar': 'home'}
    return render(request, 'tickets/home.html', context=context)


@method_decorator(login_required, name='dispatch')
class TicketCreateView(CreateView):

    model = Ticket
    fields = ['title', 'description', 'image']
    template_name = 'tickets/ticket-create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        '''
        set the user field of the ticket to the request.user before saving
        '''
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def create_review(request):
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            print(ticket, ticket.id)
            review = review_form.save(commit=False)
            review.ticket, review.user = ticket, request.user
            review.save()
            '''ticket_form.instance.user = request.user
            ticket = ticket_form.save()
            review_form.instance.user = request.user
            review_form.instance.ticket = ticket.pk
            review_form.save()'''
            return redirect(reverse('home'))
    else:
        ticket_form = forms.TicketForm()
        review_form = forms.ReviewForm()

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }

    return render(request,
                  'tickets/review-create.html',
                  context=context)
