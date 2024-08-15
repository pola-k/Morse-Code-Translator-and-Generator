from django.urls import path
from .views import morse_code_view

urlpatterns = [
    path('', morse_code_view, name='morse_code'),
]

