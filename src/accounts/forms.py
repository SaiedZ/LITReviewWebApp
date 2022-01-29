from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import UserFollows
from django.core.exceptions import ValidationError
from accounts.utils import get_followed_users


class SignupForm(UserCreationForm):
    """
    A registration form with a username and email fields
    the password field is added by the parent class
    """
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ['username', 'email']


class SubscriptionForm(forms.Form):
    """class to handle users subscriptions"""

    followed_user = forms.CharField(max_length=128,
                                    label=False)

    def __init__(self, user, *args, **kwargs):
        """
        Modify the initialization to receive the user
        at the instantiation of the form.
        """
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_followed_user(self):
        """
        Validation of the followed_user field.
        """
        username = self.cleaned_data['followed_user']
        try:
            followed_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError("L'utilisateur saisi est inconnu.")
        if self.user.username == username:
            raise ValidationError("On ne peut pas se suivre soi-même")
        followed_users = get_followed_users(self.user)
        if followed_user in followed_users:
            raise ValidationError("L'utilisateur est déjà suivi.")
        return followed_user

    def save(self):
        """
        Creates and saves a new UserFollows instance.
        """
        user_follows = UserFollows(
            user=self.user,
            followed_user=self.cleaned_data['followed_user']
        )
        user_follows.save()

        return user_follows


'''class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['user', 'followed_user']
        labels = {'followed_user': 'Utilisateur à suivre :'}
        exclude = ['user']
        widgets = {'followed_user': forms.TextInput}'''


'''class SubscriptionForm(forms.ModelForm):

    username = forms.CharField(max_length=128, required=False)

    'def __init__(self, user, *args, **kwargs):
        """
        Modify the initialization to receive the user
        at the instantiation of the form.
        """
        super().__init__(*args, **kwargs)
        self.fields['user'] = user

    class Meta:
        model = UserFollows
        fields = ['user', 'username']
        labels = {'followed_user': True}
        widgets = {'followed_user': forms.TextInput}'''
