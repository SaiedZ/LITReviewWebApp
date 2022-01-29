from typing import Any, Dict
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import CharField, Value
from itertools import chain

from tickets import forms
from tickets.models import Review, Ticket
from tickets.utils import (get_users_viewable_reviews,
                           get_users_viewable_tickets)


@login_required
def feed(request):
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    context = {'nbar': 'home', 'posts': posts}
    return render(request, 'tickets/home.html', context=context)


@login_required
def posts_user(request):
    tickets = request.user.ticket_set.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True)

    context = {"posts": posts, 'nbar': 'posts'}
    return render(request, 'tickets/my-posts.html', context=context)


@method_decorator(login_required, name='dispatch')
class TicketCreateView(CreateView):

    model = Ticket
    fields = ['title', 'description', 'image']
    template_name = 'tickets/ticket-create-update.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        '''
        set the user field of the ticket to the request.user before saving
        '''
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Créer un ticket'
        context['submit_text'] = 'Envoyer'
        return context


@login_required
def create_review(request):
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket_form.instance.user = request.user
            ticket_form.instance.answered = True
            ticket = ticket_form.save()
            review_form.instance.user = request.user
            review_form.instance.ticket = ticket
            review_form.save()
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


@method_decorator(login_required, name='dispatch')
class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = "tickets/ticket-create-update.html"
    fields = ['title', 'description', 'image']

    def get_success_url(self) -> str:
        return reverse('my-posts')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Modifier votre ticket'
        context['submit_text'] = 'Envoyer'
        return context


@method_decorator(login_required, name='dispatch')
class ReviewUpdateView(UpdateView):
    model = Review
    template_name = "tickets/review-update.html"
    form_class = forms.ReviewForm

    def get_success_url(self) -> str:
        return reverse('my-posts')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Modifier votre critique'
        return context


@method_decorator(login_required, name='dispatch')
class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = "tickets/review-ticket-delete.html"

    def get_success_url(self) -> str:
        return reverse('my-posts')

    def get_object(self, queryset=None):
        """
        Return the object
        if the user is not the creator raise Http404
        """
        obj = super().get_object(queryset=None)
        if obj.user != self.request.user:
            raise Http404(
                "Oops ! Vous n'êtes pas autorisé à supprimer cet objet !")
        return obj


@method_decorator(login_required, name='dispatch')
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "tickets/review-ticket-delete.html"

    def get_success_url(self) -> str:
        return reverse('my-posts')

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying
        if the user is not the creator raise Http404
        """
        obj = super().get_object(queryset=None)
        if obj.user != self.request.user:
            raise Http404(
                "Oops ! Vous n'êtes pas autorisé à supprimer cette objet !")
        return obj

    def form_valid(self, form):
        '''
        Set the answered attribut of the ticket to False before saving
        '''
        if self.request.user.is_authenticated:
            self.object.ticket.answered = False
            self.object.ticket.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TicketReviewCreateView(CreateView):
    model = Review
    template_name = "tickets/review-update.html"
    form_class = forms.ReviewForm

    def get_success_url(self) -> str:
        return reverse('home')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'].instance.ticket = Ticket.objects.get(
            pk=self.kwargs['pk'])
        context['page_title'] = 'Créer votre critique'
        return context

    def form_valid(self, form):
        '''
        set the ticket answered field to True before saving
        '''
        if self.request.user.is_authenticated:
            form.instance.ticket = Ticket.objects.get(pk=self.kwargs['pk'])
            form.instance.user = self.request.user
            form.instance.ticket.answered = True
            form.instance.ticket.save()
        return super().form_valid(form)
