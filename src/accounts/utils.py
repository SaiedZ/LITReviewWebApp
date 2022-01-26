from accounts.models import UserFollows


def get_followed_users(user):
    user_follows_objects = UserFollows.objects.filter(user=user)
    return [
        user_follows_object.followed_user
        for user_follows_object in user_follows_objects
    ]


def get_followers_user(user):
    user_followers_objects = UserFollows.objects.filter(followed_user=user)
    return [
        user_follower_object.user
        for user_follower_object in user_followers_objects
    ]
