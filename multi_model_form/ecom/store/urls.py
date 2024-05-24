from django.urls import path
from .views import PersonDetailUpdateView

urlpatterns = [
    path('person/<int:pk>/edit/', PersonDetailUpdateView.as_view(), name='person_detail_update_form'),
]
