from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    """
    Ticket Model
    with many to one relation with the User model
    the answered field is used to determine if user can answer
    or not a ticket. It's forbidden to review an already answered ticket
    """

    title = models.CharField(max_length=128, verbose_name='titre')
    description = models.TextField(
        max_length=2048, blank=True, verbose_name='description')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name='image')
    answered = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Le ticket '{self.title}"


class Review(models.Model):
    """
    Review Model
    with many to one relation with the User and Ticket models
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name='Note')
    headline = models.CharField(max_length=128, verbose_name='titre')
    body = models.TextField(max_length=8192,
                            blank=True,
                            verbose_name='Commentaire')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"La critique '{self.headline}"
