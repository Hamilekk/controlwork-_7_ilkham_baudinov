from django.urls import path

from webapp.view.guest import guest_create, guest_edit, guest_delete, guest_delete_confirm
from webapp.view.index import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('create_guest/', guest_create, name='create_guest'),
    path('guest/<int:pk>/edit/', guest_edit, name='edit_guest'),
    path('quest/<int:pk>/delete', guest_delete, name='guest_delete'),
    path('quest/<int:pk>/delete_confirm/', guest_delete_confirm, name='guest_delete_confirm')
]
