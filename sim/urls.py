
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('add_entry/',AddEntryView.as_view(), name='add_entry'),
    path('edit_entry/<int:entry_id>/', EditEntryView.as_view(), name='edit_entry'),
    path('delete_entry/<int:entry_id>/', DeleteEntryView.as_view(), name='delete_entry')
]
