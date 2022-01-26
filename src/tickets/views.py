from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {"user": request.user}
    return render(request, 'tickets/home.html', context=context)
