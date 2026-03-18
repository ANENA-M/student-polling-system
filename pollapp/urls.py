from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  
    path('register/', views.register_view, name='register'),  
    path('academic_subjects/', views.academic_subjects_view, name='academic_subjects'),
    path('events/', views.events_view, name='events'),
    path('school_opinion/', views.school_opinion_view, name='school_opinion'),
    path('logout/', views.logout_view, name='logout'),
    path('submit_academic_poll/', views.submit_academic_poll, name='submit_academic_poll'),
    path('submit_event_poll/', views.submit_event_poll, name='submit_event_poll'),
    path('submit_school_opinion_poll/', views.submit_school_opinion_poll, name='submit_school_opinion_poll'),
]