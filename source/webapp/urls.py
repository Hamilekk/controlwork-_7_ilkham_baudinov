from django.urls import path

from webapp.view.guest import guest_create, guest_edit
from webapp.view.index import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('create_guest/', guest_create, name='create_guest'),
    path('guest/<int:pk>/edit/', guest_edit, name='edit_guest'),
]
