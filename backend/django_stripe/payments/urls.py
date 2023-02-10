from django.urls import path

from . import views

urlpatterns = [
    path('buy/<pk>/', views.create_checkout_session)
]