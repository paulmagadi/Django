from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>', views.menu_item),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager_view/', views.manager_view),
]