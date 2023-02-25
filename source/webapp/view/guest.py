from django.shortcuts import render, redirect, get_object_or_404

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


def guest_edit(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'POST':
        form = GuestForms(request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data['name']
            guest.email = form.cleaned_data['email']
            guest.text = form.cleaned_data['text']
            guest.save()
            return redirect('index')
    else:
        guest_data = {
            'name': guest.name,
            'email': guest.email,
            'text': guest.text,
        }
        form = GuestForms(initial=guest_data)
    return render(request, 'edit_guest.html', {'form': form})
