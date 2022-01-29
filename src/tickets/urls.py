from django.urls import path
from tickets import views

urlpatterns = [
    path('home/', views.feed, name='home'),
    path('tickets/create/',
         views.TicketCreateView.as_view(),
         name='ticket-create'),
    path('reviews/create/', views.create_review, name='review-create'),
    path('my-posts/', views.posts_user, name="my-posts"),
    path('tickets/<pk>/update/',
         views.TicketUpdateView.as_view(),
         name="update-ticket"),
    path('reviews/<pk>/update/',
         views.ReviewUpdateView.as_view(),
         name="update-review"),
    path('tickets/<pk>/delete/',
         views.TicketDeleteView.as_view(),
         name="delete-ticket"),
    path('reviews/<pk>/delete/',
         views.ReviewDeleteView.as_view(),
         name='delete-review'),
    path('tickets/<pk>/create-review/',
         views.TicketReviewCreateView.as_view(),
         name='ticket-create-review'),
]
