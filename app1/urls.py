from django.shortcuts import render
from django.urls import path
from . import views
from .views import handle_response
from django.contrib.auth import views as auth_view
urlpatterns = [
        path('', views.home,name='home'),
    path('termconditions/',views.google_form_view, name='google_form_view'),
    path('handle-response/', views.handle_response, name='handle_response'),
    path('next-page/', lambda request: render(request, 'next_page.html'), name='next_page'),
    path('error-page/', lambda request: render(request, 'error_page.html'), name='error_page'),
  ]