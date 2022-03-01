from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . import utils
from . import forms


def signup_page(request):
    """Signup page view"""
    form = forms.SignupForm()

    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'accounts/signup.html', context={'form': form})


@login_required
def subscriptions_page(request, followed_id=None):
    """
    Subscription page view
    if there is a followed_id parameter it will unsubscribe from followed user
    if method is POST and form is valid, the request.user will be following
    the user with the username in the form
    """

    form = forms.SubscriptionForm(request.user)

    if followed_id:
        user_follows_object = request.user.following.filter(
            followed_user_id=followed_id)
        user_follows_object.delete()
        return redirect('subscriptions')

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
