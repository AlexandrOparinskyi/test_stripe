from django.urls import path

from . import views

urlpatterns = [
    path('buy/<pk>/', views.create_checkout_session),
    path('config/', views.config),
    path('item/<pk>/', views.index),
    path('success/', views.success),
    path('cancel/', views.cancel),
]
