from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tickets.models import Ticket


@login_required
def home(request):
    context = {"user": request.user, 'nbar': 'home'}
    return render(request, 'tickets/home.html', context=context)


@method_decorator(login_required, name='dispatch')
class TicketCreateView(CreateView):

    model = Ticket
    fields = ['title', 'description', 'image']
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        '''
        set the user field of the ticket to the request.user before saving
        '''
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
