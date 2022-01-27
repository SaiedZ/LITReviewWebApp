from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import UserFollows
from . import utils
from . import forms


def signup_page(request):
    form = forms.SignupForm()

    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'accounts/signup.html', context={'form': form})


'''def subscriptions_page(request):
    form = forms.SubscriptionForm()

    if request.method == 'POST':
        form = forms.SubscriptionForm(request.POST)
        print(form)
        if form.is_valid():
            print('hello')
            print(form.cleaned_data)
        print('request mais pas valide !')
    return render(request,
                  'accounts/subscriptions.html',
                  context={'form': form})'''


@login_required
def subscriptions_page(request, followed_id=None):
    form = forms.SubscriptionForm(request.user)

    if followed_id:
        user_model = get_user_model()
        followed_user = get_object_or_404(
            user_model,
            pk=followed_id)
        user_follows_object = UserFollows.objects.filter(
            user=request.user,
            followed_user=followed_user)
        user_follows_object.delete()

    if request.method == 'POST':
        form = forms.SubscriptionForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            form = forms.SubscriptionForm(request.user)

    followed_users = utils.get_followed_users(request.user)
    followers = utils.get_followers_user(request.user)

    return render(request,
                  'accounts/subscriptions.html',
                  context={'form': form,
                           'followed_users': followed_users,
                           'followers': followers,
                           'nbar': 'subscriptions'})
