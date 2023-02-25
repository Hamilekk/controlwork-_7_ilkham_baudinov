from django.shortcuts import render, redirect

from webapp.forms import GuestForms
from webapp.models import GuestBook


def guest_create(request):
    if request.method == 'POST':
        form = GuestForms(request.POST)
        if form.is_valid():
            guest = GuestBook(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            guest.save()
            return redirect('index')
    else:
        form = GuestForms()
    return render(request, 'guest_create.html', {'form': form})
