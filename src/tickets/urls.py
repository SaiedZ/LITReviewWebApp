from django.urls import path
from tickets import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('tickets/create/',
         views.TicketCreateView.as_view(),
         name='ticket-create'),
    path('reviews/create/', views.create_review, name='review-create')
]
