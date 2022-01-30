from django.db.models import Q

from tickets.models import Ticket, Review
from accounts.utils import get_followed_users


def get_users_viewable_tickets(user):
    """
    get all the tickes of user and followed users
    """

    followed_users = get_followed_users(user)
    return Ticket.objects.filter(
        Q(user__in=followed_users) | Q(user=user)
    )


def get_users_viewable_reviews(user):
    """get all the reviews of user, followed users
    and also from not followed users if the ticket was created
    byt the user
    """

    followed_users = get_followed_users(user)
    return Review.objects.filter(
        Q(user__in=followed_users) | Q(user=user) | Q(ticket__user=user)
        )
