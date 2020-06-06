from django.urls import path
from . import views

urlpatterns = [
    path('EndCustomer/', views.EndCustomer.as_view(), name='file-upload'),
    path('InternalUser/', views.InternalUser.as_view()),
    path('InternalUserUpdate/', views.InternalUserUpdate.as_view()),
    path('InternalUserUpdate/<int:pk>/', views.InternalUserUpdate.as_view())
]

